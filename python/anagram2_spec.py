import unittest
from anagram2 import anagrams_for

class AnagramsTest(unittest.TestCase):
    '''Test for anagram2.py'''

    def test_type(self):
        self.assertEqual(type(anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"])),list)

    def test_1(self):
        self.assertEqual(anagrams_for("saltier", ["cognac", "saltier", "realist", "retails"]),["saltier", "realist", "retails"])

    def test_2(self):
        self.assertEqual(anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]),["threads", "trashed", "hardest", "hatreds"])

    def test_3(self):
        self.assertEqual(anagrams_for("apple", ["threads", "trashed", "hardest", "hatreds", "hounds"]),[])

if __name__=='__main__':
    unittest.main()
