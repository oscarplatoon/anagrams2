# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):
	answers =[]
	for x in list_of_words:
		if(sorted(word)==sorted(x)):
			answers.append(x)
	return answers
