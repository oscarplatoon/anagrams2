import unittest

from anagram2 import anagrams_for

class TestAnagram(unittest.TestCase):

    """
    When you call anagrams_for you get a list back:
    """
    def test_returns_a_list(self):
        list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
        self.assertTrue(type(anagrams_for("threads", list_of_words)) == list)
    
    """
    When you call anagrams_for you get correct answers:
    """
    def test_anagram_function(self):
        list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
        
        list_of_numbers = ["3141", "1432", "1743", "31415"]
        
        self.assertTrue(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])

        self.assertTrue(anagrams_for("apple", list_of_words) == [])

        self.assertTrue(anagrams_for("1234", list_of_numbers) == ["1432"])

    """
    When you call the function with no arguments, you get a blank array back.
    """
    def test_function_with_default_arguments(self):
        self.assertTrue(anagrams_for() == [])

if __name__ == '__main__':
    unittest.main()
