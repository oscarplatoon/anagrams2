const sortedLettersWords = words => {
  //create result array
  let result = [];
  //iterate through word array
  for (let i = 0; i < words.length; i++) {
    let currentWord = words[i];
    let currentWordSorted = currentWord.split('').sort().join();
    result.push(currentWordSorted);
  }
  return result;
  // return result array;
}
module.exports = sortedLettersWords;