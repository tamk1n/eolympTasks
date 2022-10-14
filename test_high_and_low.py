import unittest
from high_and_low import high_and_low

class HighLowNumTest(unittest.TestCase):
  def test_highandlow(self):
    highAndlow = high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
    self.assertEqual(highAndlow, "42 0")
  
  if __name__ =="__main__":
    unittest.main()