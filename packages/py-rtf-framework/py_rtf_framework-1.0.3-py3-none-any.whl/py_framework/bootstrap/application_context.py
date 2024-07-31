from typing import Self, Any

from py_framework.config.bootstrap_config_resolver import BootstrapConfigResolver
from py_framework.config.base_config_resolver import BaseConfigResolver
import os
from py_framework.py_constants import APP_ROOT_DIR_ENV_KEY


class ApplicationContext:
    """应用配置上下文"""
    config_resolver: BaseConfigResolver


# 全局应用上下文
default_application_context: ApplicationContext


def application_context(name: str = None) -> ApplicationContext:
    """获取应用请求上下文"""
    return default_application_context


def get_config_dict_by_prefix(config_prefix: str, application_name: str = None) -> dict[str, Any]:
    """从应用配置中，根据配置前缀获取配置属性dict"""
    context: ApplicationContext = application_context(application_name)
    if context is None:
        raise ValueError(f"应用上下文对象ApplicationContext为空，请先执行bootstrap初始化")

    config_props = context.config_resolver.get_config(config_prefix)
    if config_props is None:
        error_text = f"配置前缀：{config_prefix} 下找不到配置"
        raise ValueError(error_text)

    return config_props


def get_config_value_by_key(config_key: str, application_name: str = None) -> Any:
    """从应用配置中，根据配置Key获取配置属性值"""
    context: ApplicationContext = application_context(application_name)
    if context is None:
        raise ValueError(f"应用上下文对象ApplicationContext为空，请先执行bootstrap初始化")

    config_prop = context.config_resolver.get_config(config_key)

    return config_prop


class PyApplication:
    """python应用初始化"""

    """是否启动Web"""
    _enable_web: bool = True

    """应用运行的根目录"""
    _root_dir: str = None

    def root_dir(self: Self, work_dir: str) -> Self:
        self._root_dir = work_dir if work_dir.endswith('/') else work_dir + '/'
        print('应用目录:', self._root_dir)
        return self

    def enable_web(self: Self, start_web: bool = True) -> Self:
        self._enable_web = start_web
        return self

    def run(self) -> ApplicationContext:
        global default_application_context
        default_application_context = ApplicationContext()

        # 校验根目录
        if self._root_dir is None:
            self.root_dir(os.getenv(APP_ROOT_DIR_ENV_KEY))

        # 校验是否开启web
        if not self._enable_web:
            print('禁用Web服务接口')

        default_application_context.config_resolver = BootstrapConfigResolver(base_dir=os.getcwd())

        return default_application_context
