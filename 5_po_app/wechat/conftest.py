# -*- coding:utf-8 -*-

'''
1、创建conftest.py定义日志的文件名和级别
2、pytest.ini配置 pytest日志相关项
'''

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log.log',
                    filemode='w')
