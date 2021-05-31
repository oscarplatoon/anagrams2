
def is_character_match(string1, string2):

    result = False

    # Convert to lower, split at into list at the space character
    first_string_list = string1.lower().split(" ")
    second_string_list = string2.lower().split(" ")

    # Rejoin the strings without spaces.
    first_string = "".join(first_string_list)
    second_string = "".join(second_string_list)

    # If string lengths are different, they can't be anagrams, return false
    if len(first_string) != len(second_string):
        return result

    string_dict = {}

    for i in range(len(first_string)):

        if first_string[i] in string_dict:
            string_dict[first_string[i]] += 1
        else:
            string_dict[first_string[i]] = 1

    for i in range (len(string_dict)):
        #Use the .get() to handle if character:count pair is not in string_dict.
        if(string_dict.get(second_string[i])):
            string_dict[second_string[i]] -= 1
        else:
            return result
    
    result = True
    return result