from py_framework.bootstrap.application_context import PyApplication
from py_framework.data.jdbc.jdbc_template import jdbc_template_from_config, DbType
import pandas as pd

application_context = PyApplication() \
        .enable_web(False) \
        .run()

jdbc_template = jdbc_template_from_config('application.datasource', db_type=DbType.MySql)

data_frame: pd.DataFrame = jdbc_template.queryForDF('SELECT * FROM fault_cls_dispatch_order_detail LIMIT 100');

print(data_frame.head())

jdbc_template = jdbc_template_from_config('application.ck', db_type=DbType.ClickHouse)

data_frame: pd.DataFrame = jdbc_template.queryForDF("""
    SELECT product_name , platform , series , model ,
       dispatch_day , fault_desc
    FROM svc.dispatch_order_fault_info_suanfa
    WHERE CHAR_LENGTH(fault_desc) = 6 AND dispatch_day >= '2024-06-01' AND dispatch_day <= '2024-06-01' AND product_name = '水稻机'
    ORDER BY fault_desc ASC 
""");

print(data_frame.head())