# -*- coidng:utf-8 -*-
'''
  Author : shuo
  Date : 2019/5/31 11:23
  File : connect_db.py
  Project : ClassProjects
 '''
from mysql import connector
from API_1.common.read_conf import readConf

class db_connect:

    #连接数据库的步骤：1.读取配置文件中的数据库连接信息 2.使用三方库connector连接数据库 3.获取游标 4.通过游标执行sql语句
    def connect_mysql(self,query,flag=1):
        #读取配置文件里连接数据库的sql语句
        db_config = readConf().read_caseconf('dbconfig','database')
        #连接数据库
        con = connector.connect(**db_config)
        #获取游标
        cursor = con.cursor()
        #执行sql语句
        cursor.execute(query)
        if flag == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        return res


if __name__ == '__main__':
    print(db_connect().connect_mysql('select max(Id) from loan where MemberID = 1123888'))