import unittest
from ipintel.core import classify
class Tests(unittest.TestCase):
 def test_private(self): self.assertTrue(classify('127.0.0.1')['loopback'])
if __name__=='__main__': unittest.main()
