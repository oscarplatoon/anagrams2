# Don't forget to run the tests (and create some of your own)
# split lits of words in to individual strings that can be compared to word using a for loop
# use .lower to change all characters to the same case
# sort the characters in each string a to z


def anagrams_for(word, list_of_words):
	output = []
	for tested_word in list_of_words:

		string1 = word.lower()
		string2 = tested_word.lower()
		the_tested_word=tested_word

		x = sorted(string1)
		y = sorted(string2)
		
		if x == y:
			output.append(tested_word)
		
	return output
