# -*- coding:utf-8 -*-
from test_requests.api.methods import Methods
import json

class TestHttpRequets:

    def setup(self):
        self.httpMethods = Methods()


    def testGet(self):
        params = {"a":"30","b":"40"}
        r = self.httpMethods.get(params)
        assert r.status_code == 200
        # print (type(r.json().get("args")))
        # print (type(params))
        assert (r.json().get("args")==params)


    def testPost(self):
        params = {"a": "30"}
        data = {"b": "40"}
        r = self.httpMethods.post(params=params,data=data)
        assert r.status_code == 200
        assert (r.json().get("args") == params)
        assert (json.loads(r.json().get("data")) == data)
        # print (type(r.json().get("args")))
        # print (type(params))
        # print (type(r.json().get("data")))


    def testDelete(self):
        params = {"a":"30","b":"40"}
        r = self.httpMethods.delete(params)
        assert r.status_code == 200
        # print (type(r.json().get("args")))
        # print (type(params))
        assert (r.json().get("args")==params)
