# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:34:48 2022

@author: Yigan
"""

class Node:
    
    def __init__(self):
        self.lable = ''
        self.isFinish = False
        self.edges = set()

class Edge:
    
    def __init__(self):
        self.node_from = None
        self.node_to = None
        self.label = ''
        
        
class SuffixAutomata:
    
    def __init__(self, patterns : list):
        self.prime = Node()
        self.strs = patterns
        self.__build_graph()

    def __build_graph(self):
        #TODO Build
        pass


