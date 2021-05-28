# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):
	# make variable = sorted word
	original_sorted_word = sorted(word)

	# make result list to push matching words from input list
	result_list = []
	# loop through list input and sort each word
	for word in list_of_words:
		sorted_list_word = sorted(word)
		if original_sorted_word == sorted_list_word:
			result_list.append(word)
	# return result list
	if not result_list:
		return []
	return result_list



# list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

# print(anagrams_for('apples', list_of_words))