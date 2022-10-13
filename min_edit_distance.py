# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 07:58:15 2022

@author: sriva
"""

def min_edit_distance(S1,S2,m,n):
    
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif S1[i-1]==S2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                
    return dp[m][n]

S1="SRIVA"
S2="VATSAN"
m = len(S1)
n = len(S2)
print(min_edit_distance(S1, S2, m, n))
