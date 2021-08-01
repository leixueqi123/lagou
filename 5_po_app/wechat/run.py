# -*- coding:utf-8 -*-

import pytest
import time
import subprocess
import os
import sys
'''
执行文件
调用方法：python run.py emulator-5554 4723
'''
if __name__=='__main__':
    timeslaps = time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))
    report_path = os.path.join(os.getcwd(),'report',timeslaps)
    pytest.main(['-s','-v',f'--alluredir={report_path}'])
    subprocess.Popen(['allure','serve',f'{report_path}'])


