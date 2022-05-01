# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 15:34:48 2022

@author: Yigan
"""

class Node:
    
    def __init__(self):
        self.label = 0
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
        string += "IsFinish " + str(self.isFinish)
        return string
        
        
class SuffixAutomata:
    
    def __init__(self, patterns : list):
        self.prime = Node()
        self.strs = patterns
        self.nodes = []
        self.indices = self.__build_indices()
        
        self.__build_graph()

    def __build_graph(self):
        #TODO Build
        self.prime.set_link(self.prime)
        self.nodes.append(self.prime)
        self.prime.label = '0'
        #nid = 0
        last = self.prime
        string = ""
        for s in self.strs: # TODO strs to long string
            string += s
        sid = 0
        for x in string:
            sid += 1
            p = last
            last = self.__new_node()
            
            if sid in self.indices:
                last.isFinish = True
            
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
                '''
                if sid == len(string):
                    cl.isFinish = True
                '''
                cl.len = p.len + 1
                cl.edges = q.edges
                cl.link = q.link
                last.set_link(cl)
                q.set_link(cl)
                while p.get_next(x) is q:
                    p.add_edge(x,cl)
                    p = p.link
    
    def match(self, string : str):
        curNode = self.prime
        chars = [c for c in string]
        cInd = 0
        out = []
        while cInd < len(chars):
            char = chars[cInd]
            nxtNode = curNode.get_next(char)
            if nxtNode is None:
                nxtNode = curNode.link
                curNode = nxtNode
                continue
            if nxtNode.isFinish:
                out.append(self.indices[nxtNode.len])
            curNode = nxtNode
            cInd += 1          
        
        return out
    
    def print_nodes(self):
        for n in self.nodes:
            print(n.toString())
        print(self.indices)
    
    def __new_node(self):
        node = Node()
        self.nodes.append(node)
        node.label = str(len(self.nodes)-1)
        return node
    
    def __build_indices(self):
        ma = {}
        ind = 0
        for string in self.strs:
            ind += len(string)
            ma[ind] = string
        return ma
        

patterns = ["abbcbc","ababc"]
am = SuffixAutomata(patterns)
am.print_nodes()
out = am.match("bacababcccabbcbcabababbcbc")
print(out)
