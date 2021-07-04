# -*- coding:utf-8 -*-

import pytest
import yaml
from ..pages.cal import Calculator
import logging
import os
import allure


logging.basicConfig(level=logging.INFO,filemode='w+')
logger = logging.getLogger(__name__)

def get_test_datas(mode='add'):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(path,'datas/calc.yaml')
    print (file_path)
    with open (file_path) as f:
        datas = yaml.safe_load(f)
        add_datas = datas[mode]['datas']
    return add_datas


@allure.feature("测试计算器模块")
class TestCalc:
    def setup_class(self):
        logger.info("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
         logger.info("计算结束")

    @allure.story("测试加法")
    @pytest.mark.parametrize("a,b,expect",get_test_datas())
    def test_add(self,a,b,expect):
        '''
        加法
        :param a:
        :param b:
        :param expect:
        :return:
        '''
        result = self.calc.add(a,b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect

    @allure.story("测试减法")
    @pytest.mark.parametrize("a,b,expect",get_test_datas('sub'))
    def test_sub(self,a,b,expect):
        '''
        减法
        :param a:
        :param b:
        :param expect:
        :return:
        '''
        result = self.calc.sub(a,b)
        if isinstance(result,float):
            result = round(result,2)
        assert result == expect

    @allure.story("测试乘法")
    @pytest.mark.parametrize("a,b,expect", get_test_datas('mul'))
    def test_mul(self, a, b, expect):
        '''
        乘法
        :param a:
        :param b:
        :param expect:
        :return:
        '''
        result = self.calc.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @allure.story("测试除法")
    @pytest.mark.parametrize("a,b,expect", get_test_datas('div'))
    def test_div(self, a, b, expect):
        '''
        除法
        :param a:
        :param b:
        :param expect:
        :return:
        '''
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect





