# Can you translate this driver code to unit tests?

import unittest
from anagram2 import anagrams_for

class Anagram2TestCase(unittest.TestCase):
    """Tests for armstrong_numbers.py"""

    def test_for_thread(self):
        '''Check if word have any Anagram'''
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])

    def test_for_apple(self):
        '''Check if word have any Anagram'''
        self.assertEqual(anagrams_for("apple", list_of_words), [])

if __name__ == '__main__':
    unittest.main()




list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

'''
print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
print(anagrams_for("apple", list_of_words) == [])
'''