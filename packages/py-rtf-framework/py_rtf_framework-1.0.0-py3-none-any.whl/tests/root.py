from py_framework.bootstrap.application_context import PyApplication
from py_framework.data.shaper.data_shaper import run_data_shaper

if __name__ == '__main__':
    # 启动 application_context
    application_context = PyApplication() \
        .enable_web(False) \
        .run()

    # 执行数据处理
    result_df = run_data_shaper('demo/workflow.json')

    print(result_df.head())
