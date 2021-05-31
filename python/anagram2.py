from character_match import is_character_match

def anagrams_for(word = " ", list_of_words = []):
    output = []

    for item in list_of_words:
        if is_character_match(word, item):
            output.append(item)

    return output
