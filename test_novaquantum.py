# test_novaquantum.py
"""
Tests for NovaQuantum module.
"""

import unittest
from novaquantum import NovaQuantum

class TestNovaQuantum(unittest.TestCase):
    """Test cases for NovaQuantum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaQuantum()
        self.assertIsInstance(instance, NovaQuantum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaQuantum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
