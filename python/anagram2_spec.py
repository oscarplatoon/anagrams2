import unittest

from anagram2 import anagrams_for

class TestAnagrams(unittest.TestCase) :
    
       
     
    def test_anagram_0(self) :
        self.assertEqual(anagrams_for("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]), ["threads", "trashed", "hardest", "hatreds"])
    
    def test_anagram_1(self) :
        self.assertEqual(anagrams_for("apple", ["threads", "trashed", "hardest", "hatreds", "hounds"]),  [])



if __name__ == '__main__':
    unittest.main()




# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
