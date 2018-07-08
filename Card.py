#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Card(object):
    def __init__(self,cardId,pwd,money,Lock=False):
        self.cardId = cardId
        self.cardPwd = pwd
        self.cardMoney = money
        self.lock = Lock