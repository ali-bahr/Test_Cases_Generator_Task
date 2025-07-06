import unittest
import os
import tempfile
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import read_input_file, validate_inputs, write_output_file, has_special_character

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_file.write("option1\noption2\noption3")
        self.temp_file.close()

    
    def tearDown(self):
        os.unlink(self.temp_file.name)


    def test_read_input_file(self):
        # Test reading valid input file
        options = read_input_file(self.temp_file.name)
        self.assertEqual(options, ["option1", "option2", "option3"])

        # Test reading non-existent file
        with self.assertRaises(Exception):
            read_input_file("nonexistent.txt")

    def test_has_special_character(self):
        # Test strings with special characters
        self.assertTrue(has_special_character("option@1"))
        self.assertTrue(has_special_character("option-1"))
        self.assertTrue(has_special_character("option 1"))

        # Test strings without special characters
        self.assertFalse(has_special_character("option1"))
        self.assertFalse(has_special_character("Option1"))

    def test_validate_inputs(self):
        # Test valid inputs
        valid_options = ["option1", "option2", "option3"]
        validate_inputs(valid_options)  # Should not raise any exception

        # Test empty options
        with self.assertRaises(ValueError):
            validate_inputs([])

        # Test duplicate options
        with self.assertRaises(ValueError):
            validate_inputs(["option1", "option1"])

        # Test options with special characters
        with self.assertRaises(ValueError):
            validate_inputs(["option@1"])

    def test_write_output_file(self):
        test_cases = [
            {"Master Option Of opt1": "True", "Slave Option Of opt1": "True", "ValidTC": "True"},
            {"Master Option Of opt1": "False", "Slave Option Of opt1": "True", "ValidTC": "False"}
        ]
        
        # Test writing to file
        output_file = "test_output.csv"
        write_output_file(test_cases, output_file)
        
        # Verify file exists and has correct content
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r') as f:
            content = f.read()
            self.assertIn("Test Case ID", content)
            self.assertIn("Master Option Of opt1", content)
            self.assertIn("Slave Option Of opt1", content)
            self.assertIn("ValidTC", content)
        
        # Clean up
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main() 