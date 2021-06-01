function anagramsFor(word, array) {
  var return_array = []
  for (word2 of array) {
    if ((Array.from(word.toLowerCase().replace(/\s/g, '')).sort()) == ((Array.from(word2.toLowerCase().replace(/\s/g, '')).sort()))) {
      return_array.push(word2)
    }
  } console.log(return_array)
}
var listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"]
anagramsFor('threads', listOfWords)
module.exports = anagramsFor