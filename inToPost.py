#----------------------------------------------------------------------
# inToPost.py
# Karenna Maaser
# 02/08/2009
#----------------------------------------------------------------------

from Stack import Stack

def inToPost(infixExpression):

    stack = Stack()
    postfixExpression = list()
    operator = ["*", "/", "+", "-"]

    newExpression = infixExpression.split(" ")

    for token in newExpression:
        #if type(float(token)) is float:
        try:
            value = float(token)
            postfixExpression.append(str(value))
        except ValueError:
            if token in [")", ")", ")", "(", "[", "{"]:
                pass
            elif token in operator:
                while stack.size() is not 0 and stack.top() in operator:
                    if token in operator and token >= "*" or "/":
                        item = stack.pop(stack.top())
                        postfixExpression.append(item + " ")
                    else:
                        stack.push(item)
                stack.push(token)
            else:
                topOfStack = stack.top()
                while stack.size() > 0 and topOfStack not in ["(", "[", "{"]:
                    item = stack.pop(topOfStack)
                    postfixExpression.append(item)
                    topOfStack = stack.top()
                stack.pop(topOfStack)
    while stack.size() > 0:
        item = stack.pop()
        postfixExpression.append(item + " ")
    returnValue = str()
    for i in postfixExpression:
        returnValue += i
        returnValue += " "
    return returnValue

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

def evalPostfix(postfixExpression):

    stack1 = Stack
    stack2 = Stack

    for token in postfixExpression:
        if token == "+":
        elif token == "-":
        elif token == "*":
        elif token == "/":
        else:

    pass