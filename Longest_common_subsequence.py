# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:25:51 2022

@author: sriva
"""

def lcs_algo(S1,S2,m,n):
    
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif S1[i-1]==S2[j-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
                
    ind = L[m][n]
    
    '''lcs = [""]*(ind+1)
    lcs[ind]=""
    
    i = m
    j = n
    
    while i>0 and j>0:
        
        if S1[i-1]==S2[j-1]:
            lcs[ind-1] = S1[i-1]
            i -= 1
            j -= 1
            ind -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    print("LCS :"+"".join(lcs))'''
    
    return ind
        
S1 = "BBBA"
S2 = "JJBAB"

print(lcs_algo(S1, S2, len(S1), len(S2)))

