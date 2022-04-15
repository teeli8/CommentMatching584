# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:57:29 2022

@author: Yigan
"""
import re

def remove_space(comments):
    result = [x for x in re.split(',| ', comments) if x != '']
    return result

if __name__ == '__main__':
    s= "hello, you are shit"
    str = " , this,  is a ,,, test string , , to find regex,,in js.  , ";
    print(remove_space(str))
