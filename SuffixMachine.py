# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:34:48 2022

@author: Yigan
"""

class Node:
    
    def __init__(self):
        self.label = ''
        self.len = 0
        self.link = None
        self.isFinish = False
        self.edges = dict()
    
    def get_next(self, c):
        if c not in self.edges.keys():
            return None
        return self.edges[c]
    
    def add_edge(self, c, n):
        self.edges[c] = n
    
    def set_link(self, n):
        self.link = n
    
    def toString(self):
        string = self.label + ":" + str(self.len) + " "
        for k,v in self.edges.items():
            string += k + "->" + v.label + ","
        return string
        
        
class SuffixAutomata:
    
    def __init__(self, patterns : list):
        self.prime = Node()
        self.strs = patterns
        self.nodes = []
        self.__build_graph()

    def __build_graph(self):
        #TODO Build
        self.prime.set_link(self.prime)
        self.nodes.append(self.prime)
        self.prime.label = '0'
        nid = 0
        last = self.prime
        string = self.strs # TODO strs to long string
        for x in string:
            
            p = last
            last = self.__new_node()
            last.len = p.len + 1
            while p.get_next(x) is None:
                #last.label = x              
                p.add_edge(x,last)
                p = p.link
            q = p.get_next(x)
            if q is last:
                last.set_link(self.prime)
            elif q.len == p.len + 1:
                last.set_link(q)
            else:
                cl = self.__new_node()
                cl.len = p.len + 1
                cl.edges = q.edges
                cl.link = q.link
                last.set_link(cl)
                q.set_link(cl)
                while p.get_next(x) is q:
                    p.add_edge(x,cl)
                    p = p.link
    
    def print_nodes(self):
        for n in self.nodes:
            print(n.toString())
    
    def __new_node(self):
        node = Node()
        self.nodes.append(node)
        node.label = str(len(self.nodes)-1)
        return node
        

patterns = "abbcbc"
am = SuffixAutomata(patterns)
am.print_nodes()

