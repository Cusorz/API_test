# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 20:20
  File : http_recharge.py
  Project : ClassProjects
 '''
import requests

class recharge_request:

    def requestMethod(self,method,url,params,Cookie):
        if method.upper() == 'GET':
            response = requests.get(url,params=params,cookies=Cookie) #这里必须要填写成cookies，不然会报错
        elif method.upper() == 'POST':
            response = requests.post(url,params=params,cookies=Cookie)
        else:
            print('请求方法错误')
            return None
        return response