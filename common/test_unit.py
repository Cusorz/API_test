# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 9:58
  File : test_unit.py
  Project : ClassProjects
 '''
import unittest
from ddt import ddt,data
from API_1.common.workbook import workBook
from API_1.common.http_request import httpRequest
from API_1.common.my_log import defind_mylog

registerCase = workBook('register').loading_case()
@ddt
class run_register(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @data(*registerCase)
    def test_registerCase(self,case):
        url = case['Url']
        method = case['Method']
        params = eval(case['Params'])
        #引入自定义日志模块，方便查看日志信息分析错误根源
        defind_mylog().info('现在正在运行{}模块的第{}条用例'.format(case['Moudle'],case['Caseid']))
        defind_mylog().info('测试数据是{}'.format(case))
        #发起请求
        runResult = httpRequest().request_method(url,method,params=params)
        try:
            self.assertEqual(runResult.json(),eval(case['ExpectedResult']))
            testResult = 'pass'
        except Exception as e:
            testResult = 'failed'
            defind_mylog().error(e)
            raise e
        finally:
            workBook('register').write_result(case['Caseid']+1,8,runResult.text)
            workBook('register').write_result(case['Caseid']+1,9,testResult)
# ----------------------------------------------充值--------------------------------------------------------------------
from API_1.common.http_recharge import recharge_request
from API_1.common.getData import getData
rechargeCase = workBook('recharge').loading_case()
@ddt
class run_recharge(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @data(*rechargeCase)
    def test_recharge(self,case1):
        url = case1['Url']
        method = case1['Method']
        params = eval(case1['Params'])
        # 引入自定义日志模块，方便查看日志信息分析错误根源
        defind_mylog().info('现在正在运行{}模块的第{}条用例'.format(case1['Moudle'], case1['Caseid']))
        defind_mylog().info('测试数据是{}'.format(case1))
        #发起请求
        response = recharge_request().requestMethod(method,url,params=params,Cookie=getattr(getData,'Cookie'))  #这里的cookie写的是你编写的请求方法类的参数名字，如果那里面写的是Cookie，那这里也要对应写上(注意保持一致)
        #登录之后通过反射保存cookie
        if response.cookies:
            setattr(getData,'Cookie',response.cookies)

        try:
            self.assertEqual(eval(case1['ExpectedResult']),response.json())
            testResult = 'pass'
        except Exception as e:
            defind_mylog().error(e)
            testResult = 'failed'
            raise e
        finally:
            workBook('recharge').write_result(case1['Caseid']+1,8,response.text)
            workBook('recharge').write_result(case1['Caseid']+1,9,testResult)

#------------------------------------------------加标----------------------------------------------------------------------------
from API_1.common.add_loan_workbook import add_loan

addloan_case = add_loan('addloan').load_loanCase()
@ddt
class run_addloan(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @data(*addloan_case)
    def test_addloan(self,case2):
        method = case2['Method']
        url = case2['Url']
        #查看数据里面是否包含loanid这个字段，若果有这个字段就进行替换，没有的话就直接使用原值即可（通过反射获取值）
        if case2['Params'].find('loanid') != -1:
            params = eval(case2['Params'].replace('loanid',str(getattr(getData,'loanid'))))
        else:
            params = eval(case2['Params'])
        defind_mylog().info('正在运行{}模块的{}条用例'.format(case2['Moudle'],case2['Caseid']))
        defind_mylog().info('测试数据是:{}'.format(case2['Params']))
        result = recharge_request().requestMethod(method,url,params=params,Cookie=getattr(getData,'Cookie'))
        if result.cookies:
            setattr(getData,'Cookie',result.cookies)

        try:
            self.assertEqual(eval(case2['ExpectedResult']),result.json())
            testResult = 'pass'
        except Exception as e:
            defind_mylog().error(e)
            testResult = 'failed'
            raise e
        finally:
            add_loan('addloan').write_result(case2['Caseid']+1,9,result.text)
            add_loan('addloan').write_result(case2['Caseid']+1,10,testResult)


