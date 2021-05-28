# Don't forget to run your tests!

def is_character_match(string1, string2):
	# remove all whitespace from strings
	string1 = string1.replace(" ", "")
	string2 = string2.replace(" ", "")

	# convert both strings to lower case lists of sorted characters, compare them	
	return sorted(list(string1.lower())) == sorted(list(string2.lower()))
	
