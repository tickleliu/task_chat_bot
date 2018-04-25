# -*- coding:utf-8 -*-
"""
杂项
@author:mlliu
@file: misc.py
@time: 2018/04/25 
"""

try:
    import md5 as hash
except:
    import hashlib as hash

def md5(str):
    """
    计算字符串md5
    :param str: 输入病例字符串
    :return: str的md5结果
    """
    return hash.md5(str).hexdigest()
