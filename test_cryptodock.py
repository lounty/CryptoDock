# test_cryptodock.py
"""
Tests for CryptoDock module.
"""

import unittest
from cryptodock import CryptoDock

class TestCryptoDock(unittest.TestCase):
    """Test cases for CryptoDock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoDock()
        self.assertIsInstance(instance, CryptoDock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoDock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
