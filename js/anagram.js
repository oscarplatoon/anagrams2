const sameLengthArrays = require("./sameLengthArrays");
const sortedLettersWords = require("./sortLettersInWord");
let test = "saltier";
let testArr = ["cognac", "saltier", "realist", "retails"];
// write down function that takes string word, and array of words
const anagram = (word, listOfWords) => {
  //create empty array name result
  //create variables according to helper function
  let result = [];
  let target = word.split('').sort().join('');
  // console.log(target);
  let sameLengthWords = sameLengthArrays(word, listOfWords);
  // console.log(sameLengthWords);
  let sortedArrays = sortedLettersWords(sameLengthWords);
  // console.log(sortedArrays[0]);
   //loop throught sortedArrays and push the words that match target
  for (let i = 0; i < sortedArrays.length; i++) {
    let currentWord = sortedArrays[i]
    console.log(currentWord);
    if(currentWord === target) {
      result.push(sameLengthWords[i]);
    }
  } 
  // create two helper function 
    //one that check the length of words in array and if they have same length push into new array
    //one that sort the same legnth array of words and check if the words are the same
    //create each test cases
    // return result;
  return result;
}
console.log(anagram(test,testArr))

module.exports = anagram;