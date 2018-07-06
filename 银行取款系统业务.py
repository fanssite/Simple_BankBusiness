#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
人:
类名：User
属性：name id_card phone_num
行为：

卡:
类名：Card
属性：card_id pwd
行为：

取款机:
类名：ATM
属性：
行为：new_account check deposit withdraw transfer re_pwd lock unlocking up_card cancel_account exit 

界面:
类名：Admin
属性：
行为：Admin_View Admin_login_exit Sys_Func
'''
from admin import Admin
from ATM import ATM
from collections import OrderedDict
from Card import Card
from User import User

def main():
    #管理员登入登出
    view = Admin()
    while view.Admin_login_exit():
        continue
    
    Atm = ATM()
    while True:
        view.Sys_Func()
        option = input('请选择你需要的操作:')
        if option == '1':
            #开户
            Atm.CreateUser()
        elif option == '2':
            #查询
            pass
        elif option == '3':
            #存款
            pass
        elif option == '4':
            #取款
            pass
        elif option == '5':
            #转账
            pass
        elif option == '6':
            #修改密码
            pass
        elif option == '7':
            #锁定
            pass
        elif option == '8':
            #解锁
            pass
        elif option == '9':
            #补卡
            pass
        elif option == '10':
            #销户
            pass
        elif option == 'exit':
            #退出
            if not view.Admin_login_exit():
                return -1       
if __name__=='__main__':
    allusers = OrderedDict()
    main()