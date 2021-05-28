# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):

		# your code here
	result = []
	word_chars = sorted(list(word))
	for each_word in list_of_words:
		list_word_chars = sorted(list(each_word))

		if word_chars == list_word_chars:
			result.append(each_word)

	return result

#list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

#print(anagrams_for("threads", list_of_words))
#print(anagrams_for("apple", list_of_words))