exports.isCharacterMatch = function(string1, string2) {
  /**
   * This program takes in two strings and compares them
   * Case doesn't matter, returns true if the first string can be rearranged to be the second, false otherwise.
   * Catch the edge cases:
   * str1.length > || < str2.length
   */
  let result = false
  // Convert input strings to lower case, and discard spaces.
  firstString = string1.toLowerCase()
  .split(" ").join("");
  secondString = string2.toLowerCase()
  .split(" ").join("");

  if(firstString.length !== secondString.length) return result
  let string1Chars = {};
  for (let i = 0; i<firstString.length; i++) {
    string1Chars[firstString[i]] = (string1Chars[firstString[i]] || 0) + 1
  }

  for (i = 0; i < firstString.length; i++) {
    if(string1Chars[secondString[i]]) {
      //Decrement the Object Letter:Count pair by one while iterating through the second string
      string1Chars[secondString[i]]--
    } else return result
  }
  result = true
  return result
};