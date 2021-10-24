"""
@Author  : Leixueqi
@Time    :
"""
import allure
from unittest import TestCase
from ..libs.httpclient import  HttpClient
@allure.feature("Test Weather api")
class WeatherTest(TestCase):

    def setUp(self):
        self.host = 'http://www.weather.com.cn'
        self.ep_path = '/data/cityinfo'
        self.client = HttpClient()

    @allure.story("Test of ShenZhen.")
    def test_1(self):
        city_code = '101280601'
        exp_city = '深圳'
        self.__test(city_code,exp_city)

    @allure.story("Test of BeiJing.")
    def test_2(self):
        city_code = '101280601'
        exp_city = '北京'
        self.__test(city_code,exp_city)

    @allure.story("Test of ShangHai.")
    def test_3(self):
        city_code = '101020100'
        exp_city = '上海'
        self.__test(city_code,exp_city)


    def __test(self,city_code,exp_city):
        url = f"{self.host}{self.ep_path}/{city_code}.html"
        reponse = self.client.get(url=url)
        act_city = reponse.json()['weatherinfo']['city']
        self.assertEqual(act_city==exp_city,"失败！")
