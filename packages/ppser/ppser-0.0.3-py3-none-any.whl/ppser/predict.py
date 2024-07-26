import os
from io import BufferedReader

import joblib
import numpy as np
import paddle
import yaml

from ppser import SUPPORT_MODEL
from ppser.data_utils.audio import AudioSegment
from ppser.data_utils.featurizer import AudioFeaturizer
from ppser.models import build_model
from ppser.utils.logger import setup_logger
from ppser.utils.utils import dict_to_object, print_arguments

logger = setup_logger(__name__)


class PPSERPredictor:
    def __init__(self,
                 configs,
                 model_path='models/BidirectionalLSTM_CustomFeatures/best_model/',
                 use_gpu=True):
        """
        声音分类预测工具
        :param configs: 配置参数
        :param model_path: 导出的预测模型文件夹路径
        :param use_gpu: 是否使用GPU预测
        """
        if use_gpu:
            assert paddle.is_compiled_with_cuda(), 'GPU不可用'
            paddle.device.set_device("gpu")
        else:
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
            paddle.device.set_device("cpu")
        # 读取配置文件
        if isinstance(configs, str):
            with open(configs, 'r', encoding='utf-8') as f:
                configs = yaml.load(f.read(), Loader=yaml.FullLoader)
            print_arguments(configs=configs)
        self.configs = dict_to_object(configs)
        assert self.configs.model_conf.model in SUPPORT_MODEL, f'没有该模型：{self.configs.model_conf.model}'
        # 获取特征提取器
        self._audio_featurizer = AudioFeaturizer(feature_method=self.configs.preprocess_conf.feature_method,
                                                method_args=self.configs.preprocess_conf.get('method_args', {}))
        # 获取分类标签
        with open(self.configs.dataset_conf.label_list_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.class_labels = [l.replace('\n', '') for l in lines]
        # 自动获取列表数量
        if self.configs.model_conf.model_args.get('num_class', None) is None:
            self.configs.model_conf.model_args.num_class = len(self.class_labels)
        # 获取模型
        self.predictor = build_model(input_size=self._audio_featurizer.feature_dim, configs=self.configs)
        # 加载模型
        if os.path.isdir(model_path):
            model_path = os.path.join(model_path, 'model.pdparams')
        assert os.path.exists(model_path), f"{model_path} 模型不存在！"
        self.predictor.set_state_dict(paddle.load(model_path))
        print(f"成功加载模型参数：{model_path}")
        self.predictor.eval()
        # 加载归一化文件
        self.scaler = joblib.load(self.configs.dataset_conf.dataset.scaler_path)

    def _load_audio(self, audio_data, sample_rate=16000):
        """加载音频
        :param audio_data: 需要识别的数据，支持文件路径，文件对象，字节，numpy。如果是字节的话，必须是完整的字节文件
        :param sample_rate: 如果传入的事numpy数据，需要指定采样率
        :return: 识别的文本结果和解码的得分数
        """
        # 加载音频文件，并进行预处理
        if isinstance(audio_data, str):
            audio_segment = AudioSegment.from_file(audio_data)
        elif isinstance(audio_data, BufferedReader):
            audio_segment = AudioSegment.from_file(audio_data)
        elif isinstance(audio_data, np.ndarray):
            audio_segment = AudioSegment.from_ndarray(audio_data, sample_rate)
        elif isinstance(audio_data, bytes):
            audio_segment = AudioSegment.from_bytes(audio_data)
        else:
            raise Exception(f'不支持该数据类型，当前数据类型为：{type(audio_data)}')
        # 重采样
        if audio_segment.sample_rate != self.configs.dataset_conf.dataset.sample_rate:
            audio_segment.resample(self.configs.dataset_conf.dataset.sample_rate)
        # decibel normalization
        if self.configs.dataset_conf.dataset.use_dB_normalization:
            audio_segment.normalize(target_db=self.configs.dataset_conf.dataset.target_dB)
        assert audio_segment.duration >= self.configs.dataset_conf.dataset.min_duration, \
            f'音频太短，最小应该为{self.configs.dataset_conf.dataset.min_duration}s，当前音频为{audio_segment.duration}s'
        # 获取特征
        feature = self._audio_featurizer(audio_segment.samples, sample_rate=audio_segment.sample_rate)
        # 归一化
        feature = self.scaler.transform([feature])
        feature = feature.squeeze().astype(np.float32)
        return feature

    # 预测一个音频的特征
    def predict(self,
                audio_data,
                sample_rate=16000):
        """预测一个音频

        :param audio_data: 需要识别的数据，支持文件路径，文件对象，字节，numpy。如果是字节的话，必须是完整并带格式的字节文件
        :param sample_rate: 如果传入的事numpy数据，需要指定采样率
        :return: 结果标签和对应的得分
        """
        # 加载音频文件，并进行预处理
        input_data = self._load_audio(audio_data=audio_data, sample_rate=sample_rate)
        input_data = paddle.to_tensor(input_data, dtype=paddle.float32).unsqueeze(0)
        # 执行预测
        output = self.predictor(input_data)
        result = paddle.nn.functional.softmax(output).numpy()[0]
        # 最大概率的label
        lab = np.argsort(result)[-1]
        score = result[lab]
        return self.class_labels[lab], round(float(score), 5)

    def predict_batch(self, audios_data, sample_rate=16000):
        """预测一批音频的特征

        :param audios_data: 需要预测音频的路径
        :param sample_rate: 如果传入的事numpy数据，需要指定采样率
        :return: 结果标签和对应的得分
        """
        audios_data1 = []
        for audio_data in audios_data:
            # 加载音频文件，并进行预处理
            input_data = self._load_audio(audio_data=audio_data, sample_rate=sample_rate)
            audios_data1.append(input_data)
        # 找出音频长度最长的
        batch = sorted(audios_data1, key=lambda a: a.shape[0], reverse=True)
        max_audio_length = batch[0].shape[0]
        batch_size = len(batch)
        # 以最大的长度创建0张量
        inputs = np.zeros((batch_size, max_audio_length), dtype='float32')
        for x in range(batch_size):
            tensor = audios_data1[x]
            seq_length = tensor.shape[0]
            # 将数据插入都0张量中，实现了padding
            inputs[x, :seq_length] = tensor[:]
        inputs = paddle.to_tensor(inputs, dtype=paddle.float32)
        # 执行预测
        output = self.predictor(inputs)
        results = paddle.nn.functional.softmax(output).numpy()
        labels, scores = [], []
        for result in results:
            lab = np.argsort(result)[-1]
            score = result[lab]
            labels.append(self.class_labels[lab])
            scores.append(round(float(score), 5))
        return labels, scores
