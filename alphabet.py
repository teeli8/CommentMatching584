# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:57:29 2022

@author: Yigan
"""
import re
import string


def remove_space(comments):
    punc = string.punctuation
    punc += (' ')
    for i in punc:
        comments = comments.replace(i, '')
    return comments


if __name__ == '__main__':
    s = "hello, you are shit"
    s1 = "this, is , a, test, string"

    print(remove_space(s1))
