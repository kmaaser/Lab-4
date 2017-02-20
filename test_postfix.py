#!/usr/bin/env python

#----------------------------------------------------------------------
# test_postfix.py
# Dave Reed
# 02/08/2009
#----------------------------------------------------------------------

import sys

import sys
import unittest

sys.path.insert(0, '..')
from inToPost import *

#----------------------------------------------------------------------

class PostfixTest(unittest.TestCase):

    #------------------------------------------------------------------

    def test_evalPostfix_one_op(self):

        r = evalPostfix('10.0 15.0 +')
        self.assertEqual(r, 25)
       
    #------------------------------------------------------------------

    def test_evalPostfix_sub(self):

        r = evalPostfix('10.0 15.0 -')
        self.assertEqual(r, -5.0)
       
    #------------------------------------------------------------------

    def test_evalPostfix_two_ops(self):

        r = evalPostfix('10.0 15.0 + 3.0 -')
        self.assertEqual(r, 22)

    #------------------------------------------------------------------

    def test_evalPostfix_precedence(self):

        r = evalPostfix('10.0 15.0 5.0 * +')
        self.assertEqual(r, 85)

    #------------------------------------------------------------------

    def test_evalPostfix_prec2(self):

        r = evalPostfix('10.0 15.0 + 5.5 *')
        self.assertEqual(r, 137.5)

    #------------------------------------------------------------------

    def test_evalPostfix_prec3(self):

        r = evalPostfix('10.0 15.0 + 11 5.5 - *')
        self.assertEqual(r, 137.5)

        
#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
