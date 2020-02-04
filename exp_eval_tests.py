# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01a(self):
        '''tests for value of postfix equation of +'''
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01ab(self):
        '''tests for value of postfix equation of -'''
        self.assertAlmostEqual(postfix_eval("11 5.5 -"), 5.5)

    def test_postfix_eval_01ac(self):
        '''tests for ZeroDivisionError'''
        g = "0 0 /"
        with self.assertRaises(ZeroDivisionError):
            postfix_eval(g)

        f = '1 0 /'
        with self.assertRaises(ZeroDivisionError):
            postfix_eval(f)

    def test_postfix_eval_01b(self):
        '''tests postfix for >> and <<'''
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self):
        '''tests postfix for **'''
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self):
        '''tests postfix for a combo of operands'''
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)

    def test_postfix_eval_02(self):
        '''tests for Invalid tokens'''
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

        g = 'abc'
        with self.assertRaises(PostfixFormatException):
            postfix_eval(g)

    def test_postfix_eval_03a(self):
        '''tests for insufficient operands'''
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        g = '2 -'
        with self.assertRaises(PostfixFormatException):
            postfix_eval(g)


    def test_postfix_eval_03b(self):
        '''tests for empty operands'''
        try:
            postfix_eval('')
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        g = ''
        with self.assertRaises(PostfixFormatException):
            postfix_eval(g)


    def test_postfix_eval_04(self):
        '''tests for too many operands'''
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

        g = '3 4 5 *'
        with self.assertRaises(PostfixFormatException):
            postfix_eval(g)

    def test_postfix_eval_05(self):
        '''tests for illegal bit shift operands of <<'''
        try:
            postfix_eval("123.42 -232.23 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        g = "123.42 -232.23  <<"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(g)

    def test_postfix_eval_06(self):
        '''tests for illegal bit shift operands of >>'''
        try:
            postfix_eval("123.42 -232.23 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

        g = "123.42 -232.23  >>"
        with self.assertRaises(PostfixFormatException):
            postfix_eval(g)


    def test_infix_to_postfix_01a(self):
        '''tests for infix converstion to postfix'''
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")
        self.assertEqual(infix_to_postfix(''), '')

    def test_infix_to_postfix_01b(self):
        '''tests for infix converstion to postfix'''
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self):
        '''tests for right associativity'''
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self):
        '''tests for infix converstion to postfix for a combo of operands'''
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self):
        '''tests for infix converstion to postfix when two operands are close'''
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self):
        '''tests for infix converstion to postfix'''
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self):
        '''tests for infix converstion to postfix' of negatives'''
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_prefix_to_postfix(self):
        '''tests for prefix converstion to postfix'''
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix(""), "")

    def test_prefix_to_postfix_a(self):
        '''tests for prefix converstion to postfix'''
        self.assertEqual(prefix_to_postfix("* - 3 2 1"), "3 2 - 1 *")

    def test_numeric(self):
        '''tests for numbers that include negatives, positives, and floats'''
        self.assertFalse(numeric('gg ez'), False)
        self.assertTrue(numeric('805'), True)


if __name__ == "__main__":
    unittest.main()
