#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
class Admin(object):
    def Admin_View(self):
        print(' ','*'*40)
        print('*',' '*40,'*')
        print('*',' '*40,'*')
        print('*',' '*12,'欢迎登录管理界面',' '*10,'*')
        print('*',' '*40,'*')
        print('*',' '*40,'*')
        print(' ','*'*40)


    def Admin_login_exit(self):
        admin = input('请输入管理员账号:')
        pwd =  input('请输入管理员账号密码:')
        if admin == 'admin':
            if pwd == 'admin123':
                print('操作成功,页面跳转中...')
                time.sleep(1)
                return 0
            else:
                print('密码错误，请再次输入!')
                return -1
        else:
            print('账号 有误，请确认!')
            return -1

    def Sys_Func(self):
        print(' ','*'*40)
        print('*',' '*8,'1.开户',' '*8,'2.查询',' '*8,'*')
        print('*',' '*8,'3.存款',' '*8,'4.取款',' '*8,'*')
        print('*',' '*8,'5.转账',' '*8,'6.修改密码',' '*4,'*')
        print('*',' '*8,'7.锁定',' '*8,'8.解锁',' '*8,'*')
        print('*',' '*8,'9.补卡',' '*8,'10.销户',' '*7,'*')
        print('*',' '*14,'exit退出',' '*16,'*')
        print(' ','*'*40)

