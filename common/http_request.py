# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 9:53
  File : http_request.py
  Project : ClassProjects
 '''
import requests

class httpRequest:

    def request_method(self,url,method,params):
        if method.upper() == 'GET':
            response = requests.get(url,params=params)
        elif method.upper() == 'POST':
            response = requests.post(url,params=params)
        else:
            print('暂不支持该请求方法')
            return None
        return response