exports.anagramsFor = function(word, listOfWords) {
  // sort the original word
  let originalSortedWord = word.split('').sort().join('')
  // declare an empty array to push results too
  let result = []
// loop through array of words and pick out which ones match up
  listOfWords.forEach(word =>{
    let sortedWord = word.split('').sort().join('')
    // push result the matching word
    if (originalSortedWord === sortedWord) {
      result.push(word)
    }
  });
// return result
  return result

}




