# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     tool2
   Description :
   Author :       23mofang
   date：          2020/2/22
-------------------------------------------------
   Change Activity:
                   2020/2/22:
-------------------------------------------------
"""
__author__ = 'Asdil'
def diff_set(l1, l2):
    l3 = set(l1).difference(l2)
    return l3