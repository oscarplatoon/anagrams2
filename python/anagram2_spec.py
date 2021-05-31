# Can you translate this driver code to unit tests?
import unittest
from anagram2 import anagrams_for

list_of_words = ["threads", "Trashed", "hardest", "hatreds", "hounds"]

class AnagramTestCase(unittest.TestCase):

    def test_output(self):
        self.assertIsInstance(anagrams_for("", list_of_words), list)
    
    def test_threads(self):
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])
    
    def test_apple(self):
        self.assertEqual(anagrams_for("apple", list_of_words), [])
