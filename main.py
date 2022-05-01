# -*- coding: utf-8 -*-
"""
Created on Sun May  1 14:05:52 2022

@author: Yigan
"""

from getScore import KeyWordsDict
from SuffixMachine import SuffixAutomata

file = open("patterns.txt",'r')
lines = file.readlines()
wordDict = KeyWordsDict(lines)

file2 = open("comments.txt",'r')
comment = file2.read()
comment = comment.lower()
comment = comment.replace(' ', '')
print(comment)

patterns = [l.strip().split(" ")[0] for l in lines]
print("build auto")
#print(patterns)
auto = SuffixAutomata(patterns)
print("match auto")
result = auto.match(comment)

print(result)
score = wordDict.getScore(result)
print("total score : " + str(score))
print("score : " + str(float(score) / (len(result)+0.01)))