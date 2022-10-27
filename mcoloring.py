# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 07:59:31 2022

@author: sriva
"""

class graph():
    
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]for row in range(vertices)]
    
    def issafe(self,v,color,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and color[i]==c:
                return False
        return True
    
    def graphcolorutil(self,m,color,v): 
        if v==self.V:
            return True
        
        for c in range(1,m+1):
            if self.issafe(v, color, c)==True:
                color[v]=c
                if self.graphcolorutil(m, color, v+1)==True:
                    return True
                color[v]=0
                
    def graphcoloring(self,m):
        color = [0]*self.V
        if self.graphcolorutil(m, color, 0)==None:
            return False 
        
        for c in color:
            print(c,end=' ')
        return True
    
if __name__ == '__main__':
    g = graph(4)
    g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m = 3
 
    # Function call
    g.graphcoloring(m)
    
        
        