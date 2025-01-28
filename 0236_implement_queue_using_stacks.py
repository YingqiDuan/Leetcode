############################################################
# QueueUsingStack.py 
# Implements Queue object using Stack
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
###########################################################

############################################################
#  All imports here
###########################################################
import sys # For getting Python Version
##Comment in Notebook
#from Stack import *

###########################################################
#  class  Queue using Stack
# LOOK FOR INTERFACE HERE
# LEETCODE 232
# https://leetcode.com/problems/implement-queue-using-stacks/description/

#MUST USE NAME: class QueueUsingStack
###########################################################
class MyQueue():
    def __init__(self): 
        # ONLY DATA STRUCTURE YOU CAN USE HERE IS ONLY STACK THAT YOU WROTE
        self._i=Stack()
        self._o=Stack()

    def push(self,x):
        self._i.push(x)
    
    def empty(self):
        return self._i.empty() and self._o.empty()
    
    def pop(self):
        if self.empty():
            return -1
        
        if self._o.empty():
            while not self._i.empty():
                a=self._i.pop()
                self._o.push(a)
        return self._o.pop()
    
    def peek(self):
        if self.empty():
            return -1
        
        if self._o.empty():
            while not self._i.empty():
                a=self._i.pop()
                self._o.push(a)
        return self._o.top()
    
    def __len__(self):
        return len(self._i)+len(self._o)

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
