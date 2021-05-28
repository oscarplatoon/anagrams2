# Create an array to output matches
# loop over array comparing word to list of words
# if they are anagrams, add the word in the arry to the output array
# return the output array

from character_match import is_character_match


def anagrams_for(word, list_of_words):
	output_words = []

	for x in list_of_words:
		if is_character_match(word, x):
			output_words.append(x)

	return output_words
