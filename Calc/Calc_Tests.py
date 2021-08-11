from Simple_Calc import *
import unittest

class Calc_Tests(unittest.TestCase):
    """Tests for Calc"""

    def test_number_click(self):
        """Is the number printed onto the entry"""
        calc = Simple_Calc()
        calc.number_click("9")
        expected = "9"
        actual = calc.number_entry.get().strip()
        self.assertEqual(actual, expected)

    def test_number_click_length(self):
        """Test to make sure the number is not put onto entry if it
        would exceed 18 digits/characters"""
        calc = Simple_Calc()
        #Should populate with 18 exact digits and number_click
        #should not append anything to entry
        expected = "123456789101112131"
        calc.number_entry.insert(0, expected)
        #Try to insert new
        calc.number_click("4")
        actual = calc.number_entry.get().strip()
        self.assertEqual(actual, expected)

    def test_solve_equation(self):
        """ If the entry does indeed contain a number and not characters
        first_num and operator should be assigned"""
        calc = Simple_Calc()
        calc.first_num = 4
        #Second number
        calc.number_entry.insert(0,"4")

        #addition
        calc.operator = "+"
        calc.solve_equation()
        expected = "8.0"
        actual = calc.number_entry.get().strip()
        self.assertEqual(actual, expected)

        #division
        calc.set_operator("/")
        calc.number_entry.insert(0, "4")
        calc.solve_equation()
        expected = "2.0"
        actual = calc.number_entry.get().strip()
        self.assertEqual(actual, expected)

        #multiplication
        calc.set_operator("x")
        calc.number_entry.insert(0, "8")
        calc.solve_equation()
        expected = "16.0"
        actual = calc.number_entry.get().strip()
        self.assertEqual(actual, expected)

        #subtraction
        calc.set_operator("-")
        calc.number_entry.insert(0, "2")
        calc.solve_equation()
        expected = "14.0"
        actual = calc.number_entry.get().strip()
        self.assertEqual(actual, expected)






unittest.main()
