# CellMix/__init__.py

__version__ = '0.1.7'

from .online_augmentations import get_online_augmentation, generate_demo_color_chunks

from .schedulers import patch_scheduler, ratio_scheduler

from .SoftCrossEntropyLoss import SoftCrossEntropy

from .utils import fmix, visual_usage

__all__ = ['get_online_augmentation', 'generate_demo_color_chunks', 'patch_scheduler', 'ratio_scheduler', 'SoftCrossEntropy']