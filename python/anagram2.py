def is_character_match(string1, string2):
	string1_list = list(string1)
	string2_list = list(string2)

	string1_list = sorted([x.lower() for x in string1_list])
	string2_list = sorted([x.lower() for x in string2_list])

	if string1_list == string2_list:
		return True
	else:
		return False

def anagrams_for(word_to_compare, list_of_words):
	list_to_return = []
	
	for w in list_of_words:
		if is_character_match(w, word_to_compare):
			list_to_return.append(w)

	return list_to_return