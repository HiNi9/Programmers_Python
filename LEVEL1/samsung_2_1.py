#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:38:14 2018

@author: zel0rd
"""

# 이곳에 소스코드를 작성하세요.
# Python3 만 지원됩니다.
T = int(input())
def defense():
    #temp1
    temp1 = input()
    temp1 = temp1.split()
    N = int(temp1[0])
    M = int(temp1[1])
    B = int(temp1[2])
    
    #temp2 #missile
    missile = []
    for i in range(M):
        missile.append(input())
    
    #missile = missile.split()
    print(missile)
    
    
    
for i in range(T):
    defense()
    print("-------")