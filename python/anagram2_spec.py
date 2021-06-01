# Can you translate this driver code to unit tests?

from anagram2 import anagrams_for
import unittest

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

class TestAnagram2(unittest.TestCase):

    def test_for_ana(self):
        self.assertEqual(anagrams_for('threads', list_of_words), ["threads", "trashed", "hardest", "hatreds"])

    def test_for_false(self):
        self.assertEqual(anagrams_for('apple', list_of_words), [])



if __name__ == '__main__':
    unittest.main()

# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
