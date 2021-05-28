# Don't forget to run the tests (and create some of your own)

#def anagrams_for(word, list_of_words):
		# your code here
def anagrams_for(s1, s2):
     
	output = []
	for x in range(len(s2)):
    # the sorted strings are checked
		if(sorted(s1) == sorted(s2[x])):
			output.append(s2[x])
	return output