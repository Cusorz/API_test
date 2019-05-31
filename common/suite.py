# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 10:09
  File : suite.py
  Project : ClassProjects
 '''
import unittest
from API_1.common.test_unit import run_register
from API_1.common.test_unit import run_recharge
from API_1.common.test_unit import run_addloan
import HTMLTestRunnerNew
from API_1.path.file_path import report_path

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(run_register))
# suite.addTest(loader.loadTestsFromTestCase(run_recharge))
suite.addTest(loader.loadTestsFromTestCase(run_addloan))
with open(report_path,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2)
    runner.run(suite)