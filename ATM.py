#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import random
from User import User
from Card import Card
class ATM(object):
    def __init__(self):
        self.users = dict()
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
        self.users[cardId]=user
        print('开通成功，请牢记卡号%s'%cardId)
    def SearchUserInfo(self):
        cardid = input('请输入您要查询的卡号')
        if not cardid in self.users:
            print('用户不存在在，请确认您的卡号')
            return -1
        user= self.users.get(cardid)
        if user.card.lock:
            print('卡已被锁定，请先解锁后再操作')
            return -1
        if not self.PwdCheck(user.card.cardPwd):
            user.card.lock = True
            print('密码输入错误，该卡被锁定')
            return -1
        print('账号:%s \r\n余额:%s'%(user.card.cardId,user.card.cardMoney))
    def GetMoney(self):
        pass
    def SaveMoney(self):
        pass
    def TransferMoney(self):
        pass
    def ChangePwd(self):
        pass
    def LockUser(self):
        cardid = input('请输入您要锁定的卡号')
        user = self.users.get(cardid)
        if not user:
            print('该卡不存在，锁定失败，请确认您输入的卡号是正确的')
            return -1
        if user.card.lock:
            print('该卡已被锁定，无需进行锁定操作')
        if not self.PwdCheck(user.card.cardPwd):
            print('密码输入错误，锁定失败')
            return -1
        tempIdCard = input('请输入您的身份证号码')
        if tempIdCard!=user.IdCard:
            print('身份验证失败，锁定失败')
            return -1
        else:
            user.card.lock = True
            print('锁定成功')
    def UnLocking(self):
        cardid = input('请输入您要解锁的卡号')
        user = self.users.get(cardid)
        if not user:
            print('该卡不存在，解锁失败，请确认您输入的卡号是正确的')
            return -1
        if not user.card.lock:
            print('该卡未被锁定，无需进行解锁操作')
        if not self.PwdCheck(user.card.cardPwd):
            print('密码输入错误，解锁失败')
            return -1
        tempIdCard = input('请输入您的身份证号码')
        if tempIdCard!=user.IdCard:
            print('身份验证失败，解锁失败')
            return -1
        user.card.lock = False
        print('解锁成功')
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
        if not self.users.get(str):
            return str
    def CheckprestoreMoney(self,prestoreMoney):
        if not prestoreMoney.isdigit():
            print('请勿输入数字以外的字符')
            return -1
        elif int(prestoreMoney)<=0:
            print('预存款不能小于等于0')
            return -1
        return 0
    