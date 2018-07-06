#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import random
from User import User
from Card import Card
class ATM(object):
    def __init__(self):
        self.user = dict()
    def CreateUser(self):
        username = input('请输入您的真实姓名:')
        IdCard = input('请输入您的IdCard:')
        phone = input('请输入您的电话号码:')
        while True:
            prestoreMoney = input('请输入预存款')
            if not self.CheckprestoreMoney(prestoreMoney):
                break
        password = input('请设置您的密码:')
        if not self.PwdCheck(password):
            print('密码错误，开户失败')
            return -1
            
        cardId = self.RandomCardId()
        
        card = Card(cardId,password,prestoreMoney)
        user = User(username,IdCard,phone,card)
        self.user[cardId]=user
        print('开通成功，请牢记卡号%s'%cardId)
    def SearchUserInfo(self):
        pass
    def GetMoney(self):
        pass
    def SaveMoney(self):
        pass
    def TransferMoney(self):
        pass
    def ChangePwd(self):
        pass
    def LockUser(self):
        pass
    def UnLocking(self):
        pass
    def UpCard(self):
        pass
    def CancelCard(self):
        pass
    def PwdCheck(self,password):
        for i in range(3):
            tempPwd = input('请再次输入密码:')
            if tempPwd == password:
                return True
        return False
    def RandomCardId(self):
        str = ''
        for i in range(10):
            ch = chr(random.randrange(ord('0'),ord('9')+1))
            str +=ch
        #判断是否重复
        if not self.user.get(str):
            return str
    def CheckprestoreMoney(self,prestoreMoney):
        if not prestoreMoney.isdigit():
            print('请勿输入数字以外的字符')
            return -1
        elif int(prestoreMoney)<=0:
            print('预存款不能小于等于0')
            return -1
        return 0
    