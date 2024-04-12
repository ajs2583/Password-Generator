import unittest
from Password_Generator import generate_password

class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password(self):
        # Test generating password with default parameters
        password = generate_password(10)
        self.assertEqual(len(password), 10)
        
        # Test generating password with only letters
        password = generate_password(8, include_letters=True, include_numbers=False, include_symbols=False)
        self.assertTrue(password.isalpha())
        
        # Test generating password with only numbers
        password = generate_password(6, include_letters=False, include_numbers=True, include_symbols=False)
        self.assertTrue(password.isdigit())
        
        # Test generating password with only symbols
        password = generate_password(12, include_letters=False, include_numbers=False, include_symbols=True)
        self.assertTrue(any(c in password for c in "!@#$%^&*()_+-=[]{}|;:,.<>?"))
        
        # Test generating password with all character types
        password = generate_password(14, include_letters=True, include_numbers=True, include_symbols=True)
        self.assertTrue(any(c.isalpha() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password))
        

if __name__ == '__main__':
    unittest.main()

