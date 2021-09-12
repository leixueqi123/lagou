# -*- coding:utf-8 -*-
import requests
import allure

class Methods(object):
    url = "https://httpbin.ceshiren.com/"

    @allure.step(f'{url}/get')
    def get(self,params):
        r = requests.get(f"{self.url}/get",params=params)
        #返回r,数据格式不固定，可能是xml(webservice)，json,
        return r

    @allure.step(f'{url}/post')
    def post(self,params,data):
        r = requests.post(f"{self.url}/post",params=params,json=data)
        # 返回r,数据格式不固定，可能是xml(webservice)，json,
        return r




    @allure.step(f'{url}/delete')
    def delete(self,params):
        r = requests.delete(f"{self.url}/delete",params=params)
        # 返回r,数据格式不固定，可能是xml(webservice)，json,
        return r

