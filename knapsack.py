# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:13:23 2022

@author: sriva
"""

def knapsack(W,wt,val,n):
    
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                dp[i][w]=0
            elif wt[i-1]<=w:
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]],dp[i-1][w])
            else:
                dp[i][w]= dp[i-1][w]
                
    return dp[n][W]

W = 26
wt = [12,7,11,8,9]
val = [24,13,23,15,16]
n = len(val)

print(knapsack(W, wt, val, n))
