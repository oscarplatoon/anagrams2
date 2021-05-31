import unittest

from anagram2 import anagrams_for

class TestAnagram(unittest.TestCase):

    """
    When you call anagrams_for you get a list back:
    """

    def test_returns_a_list(self):
        list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
        self.assertTrue(type(anagrams_for("threads", list_of_words)) == list)

    def test_anagram_function(self):
        list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
        
        self.assertTrue(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])

        self.assertTrue(anagrams_for("apple", list_of_words) == [])

if __name__ == '__main__':
    unittest.main()
