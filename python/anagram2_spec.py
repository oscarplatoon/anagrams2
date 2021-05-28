# Can you translate this driver code to unit tests?
import unittest
from anagram2 import anagrams_for 

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

class Anagrams2TestCase(unittest.TestCase):

    '''Test that the output is a list'''
    def test_returns_list_type(self):
        self.assertEqual(type(anagrams_for("threads", list_of_words)), list )

    def test_returns_correct_list(self):
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])
        self.assertEqual(anagrams_for("apple", list_of_words), [])


if __name__ == '__main__':
    unittest.main()
# 


# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
