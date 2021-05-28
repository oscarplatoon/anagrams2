const sameLengthArrays = require("./sameLengthArrays");

// write down function that takes string word, and array of words
const anagram = (word, listOfWords) => {
  //create empty array name result
  //create variables according to helper function
  let result = [];
  let sameLengthWords = sameLengthArrays(word, listOfWords); 
  // create two helper function 
    //one that check the length of words in array and if they have same length push into new array
    //one that sort the same legnth array of words and check if the words are the same
    //create each test cases
    // return result;
  return result;
}

module.exports = anagram;