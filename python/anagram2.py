# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):
	return_words = []
	for word2 in list_of_words:
		if (sorted(word.lower().replace(' ','')) == sorted(word2.lower().replace(' ',''))):
			return_words.append(word2)
	return return_words
