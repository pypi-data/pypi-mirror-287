import os
from .py_constants import APP_ROOT_DIR_ENV_KEY


def _load_root_dir():
    """加载模块"""
    _root_dir = __path__[0]
    os.environ[APP_ROOT_DIR_ENV_KEY] = _root_dir


def _init_app():
    """初始化应用"""
    _load_root_dir()


_init_app()
