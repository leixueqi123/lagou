【简答题】根据题干要求，在【拉勾系统】的答题框提交gitee或者github代码链接。
1、补全计算器（加法，除法）的测试用例
2、使用数据驱动完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】





leixueqi@bogon 3_pytest_homework % tree
└── calculator
    ├── __init__.py
    ├── datas  (数据驱动文件夹）
        ├── __init__.py
        └── calc.yaml (测试数据）
    ├── pages
    │    ├── __init__.py
    │    └── cal.py   （封装"加减乘除"方法）
    └── test_cases
        ├── __init__.py
        └── test_calculator.py
    ├── pytest.ini  (log日志等配置文件)
    ├── run.py   （调用时执行文件 python run.py）
    ├── report  （执行allure report文件）
    ├── log
        └── log.log （log日志文件）
    ├── README.md  