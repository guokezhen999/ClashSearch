# !/usr/bin/env python
# coding: utf-8
# @Time 2024/9/18 17:54
# @Author -郭珂桢
# @File __init__.py - py
# @Software: PyCharm

from matplotlib import pyplot as plt
import datetime

plt.rcParams['font.sans-serif']= ['Heiti TC']#防止中文乱码
plt.rcParams['axes.unicode_minus']=False#解决负号'-'显示为方块的问题

__all__ = ['plt', 'datetime']
