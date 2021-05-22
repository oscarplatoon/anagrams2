import unittest
from anagram2 import anagrams_for 

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

class TestAnagram2(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])

    def test_case_2(self):
        self.assertEqual(anagrams_for("apple", list_of_words), [])

# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
