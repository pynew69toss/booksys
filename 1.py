#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 15:07:43 2019

@author: cj
"""

import bisect
from lib.readFile import readFile
#from lib.sqluse import dbconn

c = readFile()
t='/Users/cj/booksys/booktest/bookstore1'


x=c.readpath(t)
 


#list1=[]
#bisect.insort(list1,tup1)

print(len(x)