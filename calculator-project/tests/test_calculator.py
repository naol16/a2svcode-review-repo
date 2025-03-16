import unittest
import sys

sys.path.insert(1,'C:/Users/NEZHAB/Desktop/new a2sv code review/a2svcode-review-repo/calculator-project/src')
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 1), 1)
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)
    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(5, 0),"Error: Division by zero is undefined. Please provide a non-zero denominator.") 
    
    

        
if __name__ == '__main__':
    unittest.main()