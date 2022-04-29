# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:53:15 2022

@author: Me
"""
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.operators = {'+', '-', '*', '/', '%'}
    
    def test_solve(self):
        self.assertEqual(calculator.solve(['5', '2', '+'], self.operators), ([7]))
        self.assertEqual(calculator.solve(['5', '2', '-'], self.operators), ([3]))
        self.assertEqual(calculator.solve(['5', '2', '*'], self.operators), ([10]))
        self.assertEqual(calculator.solve(['5', '2', '/'], self.operators), ([2]))
        self.assertEqual(calculator.solve(['5', '2', '%'], self.operators), ([1]))
        
        self.assertEqual(calculator.solve(['10', '28', '+', '5', '2', '-', '2', '3', '*', '4', '3', '/', '5', '2', '%', '+', '-', '*', '/'], self.operators), ([3]))
        
        with self.assertRaises(ValueError):
            calculator.solve(['1','+'], self.operators)
        
        with self.assertRaises(ZeroDivisionError):
            calculator.solve(['1', '0', '/'], self.operators)
            
    def test_validate_input_type(self):
        with self.assertRaises(TypeError):
            calculator.validate_input_type(['a', 'b', '+'], self.operators)
        with self.assertRaises(TypeError):
            calculator.validate_input_type(['1', '2', '?'], self.operators)
        with self.assertRaises(TypeError):
            calculator.validate_input_type(['a', '2', '+'], self.operators)
        with self.assertRaises(TypeError):
            calculator.validate_input_type(['1', '-1', '+'], self.operators)
            
    def test_validate_output(self):
        with self.assertRaises(ValueError):
            calculator.validate_output([-1])
        with self.assertRaises(ValueError):
            calculator.validate_output([1, 2])

if __name__ == "__main__":
    unittest.main()