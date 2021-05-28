# Can you translate this driver code to unit tests?
import unittest
from anagram2 import anagrams_for 

class Test_Anagram(unittest.TestCase):

    def test_first_case(self):
        self.assertEqual(anagrams_for("threads", list_of_words) ,["threads", "trashed", "hardest", "hatreds"])

    def test_another_case(self):
        self.assertEqual(anagrams_for("apple", list_of_words), [])
    

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)



list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])
