# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 10:28
  File : read_conf.py
  Project : ClassProjects
 '''
from configparser import ConfigParser
from API_1.path.file_path import caseConf

class readConf:
    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read(caseConf,encoding='utf-8')
    def read_caseconf(self,section,option):
        value = self.conf.get(section,option)
        return eval(value)

if __name__ == '__main__':
    print(readConf().read_caseconf('dbconfig','database'))