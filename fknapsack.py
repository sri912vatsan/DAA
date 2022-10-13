# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:27:05 2022

@author: sriva
"""

class Item:
    def __init__(self,val,weight):
        self.val = val
        self.weight = weight
        
def fractionalKnapsack(W,arr):
    
    arr.sort(key=lambda x: (x.val/x.weight),reverse=True)
    
    final_val = 0.0
    
    for item in arr:
        
        if item.weight<=W:
            W -= item.weight
            final_val += item.val
        else:
            final_val += item.val * W/item.weight
            break
        
    return final_val

if __name__ == "__main__":
    
    W = 50
    arr = [Item(60,20),Item(100,50),Item(120,30)]
    
    print(fractionalKnapsack(W, arr))
        
        