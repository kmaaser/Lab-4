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

    # precedence
    importance = {"*": 1,
                  "/": 1,
                  "+": 0,
                  "-": 0}

    # splits the expression at the spaces
    newExpression = infixExpression.split()

    # goes through the expression
    for token in newExpression:
        if token.replace(".","",1).isdigit():
            postfixExpression += (token+" ")
        # if the token is a left parentheses
        elif token in ["(", "[", "{"]:
            stack.push(token)
        # if the token is in the operator
        elif token in operator:
            # checks the size
            # checks what is on the top of the stack
            # checks the importance of the top of stack vs the token
            while stack.size() != 0 and stack.top() in "*/+-" and (importance[stack.top()] >= importance[token]):
                postfixExpression += stack.pop() + " "
            stack.push(token)

        else:
            # if the top of the stack is a left parentheses
            while stack.top() not in ["(", "[", "{"]:
                postfixExpression += stack.pop() + " "
            stack.pop()
    postfixExpression+= stack.pop()+" "

    while stack.size()!=0:
        postfixExpression += stack.pop() + " "
    # returns the postExpression
    return postfixExpression
#----------------------------------------------------------------------

def evalPostfix(postfixExpression):

    # creates an empty stack
    # keeps track of answer
    numStack = Stack()
    answer = 0
    operator = ["*", "/", "+", "-"]
    # splits the postExpression
    postList = postfixExpression.split()

    for token in postList:
        if token in operator:
            # pops two numbers off of the stack
            item1 = eval(numStack.pop())
            item2 = eval(numStack.pop())
            # performs the correct operation depending on what operator is is
            # then pushes the answer back on the stack
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
        # if the token is not a operator
        else:
            numStack.push(token)
    answer = eval(numStack.pop())
    # returns the "answer"
    return answer