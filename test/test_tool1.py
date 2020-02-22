# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_tool1
   Description :
   Author :       23mofang
   date：          2020/2/22
-------------------------------------------------
   Change Activity:
                   2020/2/22:
-------------------------------------------------
"""
__author__ = 'Asdil'
from impute_test import tool1

def test_inter_set():
    l1 = [1,2,3,4,5]
    l2 = [1,2,3,4,5]
    assert len(tool1.inter_set(l1, l2))== 5
