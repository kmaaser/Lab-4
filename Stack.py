#!/usr/bin/env python
# Stack.py
# Dave Reed
# CS161
# 02/24/2006

#----------------------------------------------------------------------

class Stack(object):

    #------------------------------------------------------------------

    def __init__(self):

        '''creates an empty stack'''
                
        self.items = []

    #------------------------------------------------------------------

    def push(self, x):

        '''places x on top of the stack

        pre: none

        post: x is placed on top of the stack'''
        
        self.items.append(x)

    #------------------------------------------------------------------

    def pop(self):

        '''removes and returns the top element of the stack

        pre: stack is not empty; raises IndexError if empty

        post: removes and returns top item of stack'''


        return self.items.pop()

    #------------------------------------------------------------------

    def top(self):

        '''returns the top element of the stack without removing it

        pre: stack is not empty; raises IndexError if empty

        post: returns top item of stack'''

        return self.items[self.size()-1]

    #------------------------------------------------------------------

    def size(self):

        '''returns the number of elements in the stack

        pre: none

        post: returns the number of elements in the stack'''
        
        return len(self.items)

#----------------------------------------------------------------------
