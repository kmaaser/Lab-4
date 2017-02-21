#----------------------------------------------------------------------
# inToPost.py
# Karenna Maaser
# 02/08/2009
#----------------------------------------------------------------------

from Stack import Stack

def breakUpExpression:

    pass

def parensBalance(s):
    stack = Stack()
    for ch in s:
        if ch in "({[":     # push an opening marker
            stack.push(ch)
        elif ch in ")}]":
            if stack.size() < 1:
                return False
            else:
                opener = stack.pop()
                if opener+ch not in ["()", "[]", "{}"]:
                    return False
    return stack.size() == 0 # an empty stack means that everything is matched up

def evalPostfix:

    pass