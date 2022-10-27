# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 07:16:32 2022

@author: sriva
"""

global N
N = 4

def printsoln(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()

def issafe(b,row,col):
    
    for i in range(col):
        if b[row][i]==1:
            return False
        
    for i,j in zip(range(row,-1,-1),
                   range(col,-1,-1)):
        if b[i][j]==1:
            return False
            
    for i,j in zip(range(row,N,1),
                   range(col,-1,-1)):
        if b[i][j]==1:
            return False
        
    return True

def solveNQUtil(b,col):
    
    if col >= N:
        return True
    
    for i in range(N):
        
        if issafe(b,i,col):
            
            b[i][col]=1
            
            if solveNQUtil(b,col+1)==True:
                return True 
            
            b[i][col]=0
            
    return False

def solveNQ():
    board = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    
    if solveNQUtil(board, 0)==False:
        print("No solution")
        return False
    
    printsoln(board)
    return True

solveNQ()
        