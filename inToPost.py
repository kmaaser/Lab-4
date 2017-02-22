#----------------------------------------------------------------------
# inToPost.py
# Karenna Maaser
# 02/08/2009
#----------------------------------------------------------------------

from Stack import Stack

def inToPost():

    stack = Stack()
    expression = list()
    postfixExpression = list()
    operator = ["*", "/", "+", "-"]
    for token in expression:
        if token == int:
            postfixExpression.append(token)
        elif token == ["(", "[", "{"]:
            stack.push(token)
        elif token == ["*", "/", "+", "-"]:
            while stack.size != 0 and stack.top() == operator:
                if stack.top() == ["*", "/"]:
                    stack.pop(stack.top())
                    postfixExpression.append(stack.top() + " ")
            stack.push(token)
        else:
            while stack.size() > 0 and stack.top != [")", "]", "}"]:
                stack.pop(stack.top())
                postfixExpression.append(stack.top())
            stack.pop(stack.top())
    while stack.size > 0:
        stack.pop()
        postfixExpression.append(token + " ")

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