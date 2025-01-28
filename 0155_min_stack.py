############################################################
# MinStack.py 
# Implements MinStack
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2022
###########################################################
############################################################
# MinStack.py 
# Implements MinStack
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2022
###########################################################

############################################################
#  All imports here
###########################################################
import sys # For getting Python Version
##Comment in Notebook
#from Stack import *

###########################################################
#  Min Stack

#LOOK FOR INTERFACE HERE: 
# LEETCODE 155
# https://leetcode.com/problems/min-stack/description/


#MUST USE NAME: class MinStack
###########################################################
class MinStack():
    def __init__(self): 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY STACK THAT YOU WROTE
        self._a=Stack()
        self._m=Stack()
    
    def push(self,x):
        self._a.push(x)
        if self._m.empty() or x<=self._m.top():
            self._m.push(x)

    def pop(self):
        if self._a.empty():
            return
        i=self._a.pop()
        if not self._m.empty() and i==self._m.top():
            self._m.pop()
    
    def top(self):
        if self._a.empty():
            return -1
        return self._a.top()
    
    def empty(self)->'bool':
        return self._a.empty()
    
    def getMin(self):
        if self._m.empty():
            return None
        return self._m.top()

############################################################
# Stack.py 
# Implements Stack object
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
###########################################################

###########################################################
#  class  Stack
# Our stack is infinite size
# implement push, pop, top, empty, isfull, space  and len
# space is the max space used at any time. 
###########################################################   
class Stack:
    def __init__(self):
        self._a = []      
        self._n = 0       
        self._max_size = 0  

    def push(self, item):
        self._a[self._n : self._n] = [item]
        self._n += 1
        if self._n > self._max_size:
            self._max_size = self._n

    def pop(self):
        if self._n == 0:
            raise IndexError
        top_item = self._a[self._n - 1]
        self._a[self._n - 1 : self._n] = []
        self._n -= 1
        return top_item

    def top(self):
        if self._n == 0:
            raise IndexError
        return self._a[self._n - 1]

    def empty(self):
        return (self._n == 0)

    def isfull(self):
        return False

    def space(self):
        return self._max_size

    def __len__(self):
        return self._n
