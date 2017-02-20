#!/usr/bin/env python

#----------------------------------------------------------------------
# test_inToPost.py
# Dave Reed
# 03/08/2005
#----------------------------------------------------------------------

import sys

import sys
import unittest

sys.path.insert(0, '..')
from inToPost import *

#----------------------------------------------------------------------

class InToPostTest(unittest.TestCase):

    #------------------------------------------------------------------

    def test_i2p_one_op(self):

        s = inToPost('10 + 15')
        s = s.strip()
        self.assertEqual(s == '10 15 +' or s == '10.0 15.0 +', True)

    #------------------------------------------------------------------

    def test_i2p_two_ops(self):

        s = inToPost('10 + 15 - 3')
        s = s.strip()
        self.assertEqual(s == '10 15 + 3 -' or s == '10.0 15.0 + 3.0 -', True)

    #------------------------------------------------------------------

    def test_i2p_precedence(self):

        s = inToPost('10 + 15 * 5')
        s = s.strip()
        self.assertEqual(s == '10 15 5 * +' or s == '10.0 15.0 5.0 * +', True)

    #------------------------------------------------------------------

    def test_i2p_paren(self):

        s = inToPost('( 10 + 15 ) * 5')
        s = s.strip()
        self.assertEqual(s == '10 15 + 5 *' or s == '10.0 15.0 + 5.0 *', True)

    #------------------------------------------------------------------

    def test_i2p_float(self):

        s = inToPost('( 10 + 15 ) * 5.5')
        s = s.strip()
        self.assertEqual(s == '10 15 + 5.5 *' or s == '10.0 15.0 + 5.5 *', True)

    #------------------------------------------------------------------

    def test_i2p(self):
        s = inToPost('2 * ( ( 3 + 4 ) * 2 + 3 ) - 5 * 3 + 6 / 2')
        s = s.strip()
        self.assertEqual(s == '2 3 4 + 2 * 3 + * 5 3 * - 6 2 / +' or \
                         s == '2.0 3.0 4.0 + 2.0 * 3.0 + * 5.0 3.0 * - 6.0 2.0 / +', True)
    
    #------------------------------------------------------------------

    def test_evalPostfix_one_op(self):

        r = evalPostfix('10.0 15.0 +')
        self.assertEqual(r, 25)
       
    #------------------------------------------------------------------

    def test_evalPostfix_two_ops(self):

        s = inToPost('10 + 15 - 3')
        r = evalPostfix('10.0 15.0 + 3.0 -')
        self.assertEqual(r, 22)

    #------------------------------------------------------------------

    def test_evalPostfix_precedence(self):

        r = evalPostfix('10.0 15.0 5.0 * +')
        self.assertEqual(r, 85)

    #------------------------------------------------------------------

    def test_evalPostfix_float(self):

        r = evalPostfix('10.0 15.0 + 5.5 *')
        self.assertEqual(r, 137.5)

        
#----------------------------------------------------------------------

def main(argv):
    unittest.main()

#----------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)
