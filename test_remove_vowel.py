import unittest
from remove_vowel import removevowel

class CommentTestCase(unittest.TestCase):
  def test_comment(self):
    removed_vowel = removevowel("This is the best fucking app ever!!!")
    self.assertEqual(removed_vowel, "Ths s th bst fckng pp vr!!!")

if __name__ == '__main__':
  unittest.main()

