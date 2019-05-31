# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 9:24
  File : file_path.py
  Project : ClassProjects
 '''
import os

path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
api_path = os.path.join(path,'testCase','api.xlsx')
report_path = os.path.join(path,'report','test_report.html')
caseConf = os.path.join(path,'conf','caseConf.conf')
logConf = os.path.join(path,'report','logConf.log')
# print(caseConf)