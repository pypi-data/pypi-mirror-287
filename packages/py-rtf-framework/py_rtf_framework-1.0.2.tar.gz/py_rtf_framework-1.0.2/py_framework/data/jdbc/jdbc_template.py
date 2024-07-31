from enum import Enum
from .base_jdbc_template import BaseJdbcTemplate, DbConfig
from py_framework.bootstrap.application_context import application_context, ApplicationContext
from py_framework.data.jdbc.mysql_jdbc_template import MysqlJdbcTemplate
from py_framework.data.jdbc.clickhouse_jdbc_template import ClickhouseJdbcTemplate


class DbType(str, Enum):
    """数据库类型"""

    MySql = "mysql"
    ClickHouse = "clickhouse"


def jdbc_template_from_config(config_prefix: str, db_type: DbType) -> BaseJdbcTemplate:
    """获取mysql的操作模板"""
    context: ApplicationContext = application_context()
    if context is None:
        raise ValueError(f"应用上下文对象ApplicationContext为空，请先执行bootstrap初始化")

    config_props = context.config_resolver.get_config(config_prefix)
    if config_props is None:
        error_text = f"配置前缀：{config_prefix} 下找不到{db_type}相关配置"
        raise ValueError(error_text)

    db_config = DbConfig(**config_props)

    print(config_prefix, 'db连接配置: ', db_config.json())

    if db_type == DbType.MySql:
        jdbc_template = MysqlJdbcTemplate(db_config)
    elif db_type == DbType.ClickHouse:
        jdbc_template = ClickhouseJdbcTemplate(db_config)
    else:
        raise ValueError('不支持' + db_type + "创建jdbcTemplate")

    return jdbc_template
