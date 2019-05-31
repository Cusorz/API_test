# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/30 11:01
  File : my_log.py
  Project : ClassProjects
 '''
import logging
from API_1.path.file_path import logConf

class defind_mylog:
    def logger(self,level,msg):
        logger = logging.getLogger('mylogger')
        logger.setLevel('DEBUG')

        console_handle = logging.StreamHandler()
        console_handle.setLevel('DEBUG')

        file_handle = logging.FileHandler(logConf,encoding='utf-8')
        file_handle.setLevel('DEBUG')

        logger.addHandler(console_handle)
        logger.addHandler(file_handle)

        if level == 'DEBUG':
            logger.debug(msg)
        elif level == 'INFO':
            logger.info(msg)
        elif level == 'WARNING':
            logger.warning(msg)
        elif level == 'ERROR':
            logger.error(msg)
        else:
            logger.critical(msg)

        logger.removeHandler(file_handle)
        logger.removeHandler(console_handle)


    def debug(self,msg):
        self.logger('DEBUG',msg)

    def info(self,msg):
        self.logger('INFO',msg)

    def warning(self,msg):
        self.logger('WARNING',msg)

    def error(self,msg):
        self.logger('ERROR',msg)

    def critical(self,msg):
        self.logger('CRITICAL',msg)

if __name__ == '__main__':
    print(defind_mylog().error('这是错误信息'))