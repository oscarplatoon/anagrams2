# Can you translate this driver code to unit tests?
import unittest
from anagram2 import anagrams_for 

class Anagrams2TestCase(unittest.TestCase):
    """Tests for anagram2.py"""

    def test_anagrams_returns_a_list(self):
        """When you call anagram_for(), you should get a list back"""
        self.assertIsInstance(anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]), list)

    def test_anagrams_for_correct_output(self):
        """
        Verify that correct anagrams are found
        """
        self.assertListEqual(anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]), ["threads", "trashed", "hardest", "hatreds"])

    def test_anagrams_for_incorrect_output(self):
        """ Verify no anagrams found """
        self.assertListEqual(anagrams_for("apple", ["threads", "trashed", "hardest", "hatreds", "hounds"]), [])


if __name__ == '__main__':
    unittest.main()

# list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
