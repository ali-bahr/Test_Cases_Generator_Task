import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import run_test_case, generate_test_cases

class TestMain(unittest.TestCase):
    def test_run_test_case(self):
        # Test case 1: Valid test case
        test_case1 = {
            "Master Option Of opt1": "True",
            "Slave Option Of opt1": "True",
            "Master Option Of opt2": "False",
            "Slave Option Of opt2": "False"
        }
        run_test_case(test_case1, ["opt1", "opt2"])
        self.assertEqual(test_case1["ValidTC"], "True")
        self.assertEqual(test_case1["Expected Of opt1"], "True")
        self.assertEqual(test_case1["Expected Of opt2"], "False")

        # Test case 2: Invalid test case
        test_case2 = {
            "Master Option Of opt1": "True",
            "Slave Option Of opt1": "False",
            "Master Option Of opt2": "False",
            "Slave Option Of opt2": "False"
        }
        run_test_case(test_case2, ["opt1", "opt2"])
        self.assertEqual(test_case2["ValidTC"], "False")

        # Test case 3: NA values
        test_case3 = {
            "Master Option Of opt1": "NA",
            "Slave Option Of opt1": "True",
            "Master Option Of opt2": "False",
            "Slave Option Of opt2": "NA"
        }
        run_test_case(test_case3, ["opt1", "opt2"])
        self.assertEqual(test_case3["ValidTC"], "True")
        self.assertEqual(test_case3["Expected Of opt1"], "True")
        self.assertEqual(test_case3["Expected Of opt2"], "False")

    def test_generate_test_cases(self):
        options = ["opt1", "opt2"]
        test_cases = generate_test_cases(options)
        
        # Verify the number of test cases (should be 3^4 = 81 for 2 options)
        self.assertEqual(len(test_cases), 81)
        
        # verify structure of first test case
        first_case = test_cases[0]
        self.assertIn("Master Option Of opt1", first_case)
        self.assertIn("Slave Option Of opt1", first_case)
        self.assertIn("Master Option Of opt2", first_case)
        self.assertIn("Slave Option Of opt2", first_case)
        self.assertIn("ValidTC", first_case)
        self.assertIn("Expected Of opt1", first_case)
        self.assertIn("Expected Of opt2", first_case)

if __name__ == '__main__':
    unittest.main()