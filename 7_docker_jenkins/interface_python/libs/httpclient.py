"""
@Author  : Leixueqi
@Time    :
"""
import requests
import urllib3

class HttpClient:

    def __init__(self,disable_ssl_verify=False,timeout=50):
        self.client  = requests.session()
        self.disable_ssl_verify = disable_ssl_verify
        self.timeout = timeout

        if self.disable_ssl_verify:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarining)


    def get(self,url,headers=None,data=None,json=None,params=None,*args,**kwargs):
        if headers is None:
            headers = {}
        if self.disable_ssl_verify:
            reponse = self.client.get(url,headers=headers,data=data,json=json,params=params,\
            verify=False,timeout=self.timeout,*args,**kwargs)
        else:
            reponse = self.client.get(url,headers=headers,data=data,json=json,params=params,\
            timeout=self.timeout,*args,**kwargs)

        reponse.encoding = 'utf-8'
        print (f'{reponse.json()}')
        return reponse


    def post(self,url,headers=None,data=None,json=None,params=None,*args,**kwargs):
        if headers is None:
            headers = {}
        if self.disable_ssl_verify:
            reponse = self.client.get(url,headers=headers,data=data,json=json,params=params,\
            verify=False,timeout=self.timeout,*args,**kwargs)
        else:
            reponse = self.client.get(url,headers=headers,data=data,json=json,params=params,\
            timeout=self.timeout,*args,**kwargs)

        reponse.encoding = 'utf-8'
        print (f'{reponse.json()}')
        return reponse