#----------------------------------------------------------------------
# inToPost.py
# Karenna Maaser
# 02/08/2009
#----------------------------------------------------------------------

from Stack import Stack

def inToPost(s):

    open = 0
    for ch in s:
        if ch == '([{':
            open =+1
        elif ch == ')]}':
            open -= 1
            if open < 0:
                # there is no matching opener, so check fails
                return False
    return open == 0 # everything balances if no unmatched opens

def evalPostfix:

    pass