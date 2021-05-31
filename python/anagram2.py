# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):


	# create empty list to append matches to
	# lower & sort input string

	new_list = []
	word_lowered = "".join(sorted(word.lower()))

	# lower original list in case case isn't consistent for input list

	# sort lowered list for comparison to sorted input string

	# append matches to new list for output
	
	lowered_words = [w.lower() for w in list_of_words]
	sorted_words = [ "".join(sorted(w)) for w in lowered_words]
	for w in range(len(sorted_words)):
		if word_lowered == sorted_words[w]:
			new_list.append(lowered_words[w])
	
	return new_list
