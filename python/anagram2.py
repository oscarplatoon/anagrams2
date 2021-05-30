



def anagrams_for(word, list_of_words):
	
	answer = []
	# Split the word into a list
	new_list = (list(word))

	# Sort the word 	
	word = (sorted(new_list))
	# Loop through the array
	# Sort each item
	# Compare with word
	# Append to answer	
	for x in list_of_words:
		if word == (sorted(x)) :
			answer.append(x)
		
	
	return answer
	
	