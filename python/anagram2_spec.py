# Can you translate this driver code to unit tests?

import unittest
from anagram2 import anagrams_for 

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

#print(anagrams_for("threads", list_of_words) == ["threads", "trashed", #"hardest", "hatreds"])
#print(anagrams_for("apple", list_of_words) == [])


class AnagramTestCase(unittest.TestCase):
    """Tests for anagram2.py"""

    def test_is_anagram(self):
        """When you call anagram2(), you should get a list back"""
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])

    def test_not_an_anagram(self):
        """When you call anagram2(), you should get a list back"""
        self.assertEqual(anagrams_for("apple", list_of_words), [])

if __name__ == '__main__':
    unittest.main()