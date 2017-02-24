#----------------------------------------------------------------------
# inToPost.py
# Karenna Maaser
# 02/23/2017
#----------------------------------------------------------------------

from Stack import Stack

def inToPost(infixExpression):

    # Creates a new stack
    # Creates a new list
    stack = Stack()
    postfixExpression = ""
    operator = ["*", "/", "+", "-"]
    importance = {"*": 1,
                  "/": 1,
                  "+": 0,
                  "-": 0}

    # splits the expression at the spaces
    newExpression = infixExpression.split()
    print(newExpression)

    # goes through the expression
    for token in newExpression:
        print (postfixExpression)
        print (stack.items)
        if token.replace(".","",1).isdigit():
            postfixExpression += (token+" ")
        elif token in ["(", "[", "{"]:
            stack.push(token)
        # if the token is in the operator
        elif token in operator:
            while stack.size() != 0 and stack.top() in "*/+-" and (importance[stack.top()] >= importance[token]):
                postfixExpression += stack.pop() + " "
            stack.push(token)

        else:
            while stack.top() not in ["(", "[", "{"]:
                print(stack.items)
                postfixExpression += stack.pop() + " "
            stack.pop()
    postfixExpression+= stack.pop()+" "
    while stack.size()!=0:
        postfixExpression += stack.pop() + " "
    print (postfixExpression)
    return postfixExpression


def evalPostfix(postfixExpression):

    numStack = Stack()
    answer = 0
    operator = ["*", "/", "+", "-"]
    postList = postfixExpression.split()

    for token in postList:
        if token in operator:
            item1 = eval(numStack.pop())
            item2 = eval(numStack.pop())
            if token == "+":
                answer = (item1 + item2)
                numStack.push(str(answer))
            elif token == "-":
                answer = (item2 - item1)
                numStack.push(str(answer))
            elif token == "*":
                answer = (item1 * item2)
                numStack.push(str(answer))
            elif token == "/":
                answer = (item2 / item1)
                numStack.push(str(answer))
        else:
            numStack.push(token)
    answer = eval(numStack.pop())
    return answer