# test_ghostspirit.py
"""
Tests for GhostSpirit module.
"""

import unittest
from ghostspirit import GhostSpirit

class TestGhostSpirit(unittest.TestCase):
    """Test cases for GhostSpirit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GhostSpirit()
        self.assertIsInstance(instance, GhostSpirit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GhostSpirit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
