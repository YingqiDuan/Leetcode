############################################################
# Queue.py 
# Implements Queue object
# Author: Jagadeesh Vasudevamurthy
# Copyright: Jagadeesh Vasudevamurthy 2025
###########################################################

###########################################################
#  class Queue
# Our Queue is finite size k
# Leetcode 622
# Look for interface here: https://leetcode.com/problems/design-circular-queue/
# MUST USE Name: class Queue()
###########################################################   
class MyCircularQueue():
    def __init__(self,k:'int'):
        # You must use Python List
        # Must use all spaces
        self._a = [None]*k #CANNOT CHANGE THIS. k space is already allocated
        self._MAX = k
        ## YOU CAN HAVE YOUR PRIVATE DATA MEMBER HERE
        self._front=0
        self._rear=-1
        self._size=0
        
        
    def enQueue(self, T)->'bool':
        ## YOU CANNOT CALL append in this routine as U already have enough space
        ## YOU CAN DO: self._a[pos] = T #pos is some position between 0 to self._MAX-1
        if self.isFull():
            return False
        
        self._rear=(self._rear+1)%self._MAX
        self._a[self._rear]=T
        self._size+=1
        return True
        
    def Front(self)->'T':
        ## YOU CANNOT CALL pop(0). NOTE: pop(0) is O(n). We want THETA(1)
        if self.isEmpty():
            return -1
        return self._a[self._front]
        
    ## WRITE ALL OTHER ROUTINES
    def isFull(self) -> 'bool':
        return (self._size == self._MAX)
    
    def deQueue(self)->'bool':
        if self.isEmpty():
            return False
        
        self._front = (self._front + 1) % self._MAX
        self._size -= 1
        return True
    
    def isEmpty(self) -> 'bool':
        return (self._size == 0)
    
    def Rear(self) -> 'int':
        if self.isEmpty():
            return -1
        return self._a[self._rear]

    
    #Print from FRONT TO REAR
    def __str__(self)->'string':
        s = ""
        ## WRITE CODE HERE
        if self.isEmpty():
            return "[]"
        
        res=[]
        for i in range(self._size):
            j=(self._front+i)%self._MAX
            res.append(str(self._a[j]))
        return "[" + ", ".join(res) + "]"
        
    def __len__(self)->'int':
        return self._size
    