import importlib

from paddle.optimizer import *
from .scheduler import cosine_decay_with_warmup as WarmupCosineSchedulerLR
from paddle.optimizer.lr import *
from ppser.utils.logger import setup_logger

logger = setup_logger(__name__)

__all__ = ['build_optimizer', 'build_lr_scheduler']


def build_optimizer(parameters, learning_rate, configs):
    use_optimizer = configs.optimizer_conf.get('optimizer', 'Adam')
    optimizer_args = configs.optimizer_conf.get('optimizer_args', {})
    optim = importlib.import_module(__name__)
    optimizer = getattr(optim, use_optimizer)(parameters=parameters, learning_rate=learning_rate, **optimizer_args)
    logger.info(f'成功创建优化方法：{use_optimizer}，参数为：{optimizer_args}')
    return optimizer


def build_lr_scheduler(step_per_epoch, configs):
    use_scheduler = configs.optimizer_conf.get('scheduler', 'WarmupCosineSchedulerLR')
    scheduler_args = configs.optimizer_conf.get('scheduler_args', {})
    if configs.optimizer_conf.scheduler == 'CosineAnnealingDecay' and 'T_max' not in scheduler_args:
        scheduler_args.T_max = int(configs.train_conf.max_epoch * 1.2) * step_per_epoch
    if configs.optimizer_conf.scheduler == 'WarmupCosineSchedulerLR' and 'fix_epoch' not in scheduler_args:
        scheduler_args.fix_epoch = configs.train_conf.max_epoch
    if configs.optimizer_conf.scheduler == 'WarmupCosineSchedulerLR' and 'step_per_epoch' not in scheduler_args:
        scheduler_args.step_per_epoch = step_per_epoch
    optim = importlib.import_module(__name__)
    scheduler = getattr(optim, use_scheduler)(**scheduler_args)
    logger.info(f'成功创建学习率衰减：{use_scheduler}，参数为：{scheduler_args}')
    return scheduler
