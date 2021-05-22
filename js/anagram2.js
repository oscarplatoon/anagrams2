function anagramsFor(wordToCompare, listOfWords) {
  let arrayToReturn = [];

  for (let i = 0; i < listOfWords.length; i++) {  // make sure to have 'let' for i
    console.log(wordToCompare, listOfWords[i]);
    if (isCharacterMatch(wordToCompare, listOfWords[i])) {
      arrayToReturn.push(listOfWords[i]);
    }
  }

  return arrayToReturn;
}

function isCharacterMatch(string1, string2) {
  let stringArray1 = string1.split("");
  let stringArray2 = string2.split("");

  let lowerCaseArray1 = stringArray1.map(x => x.toLowerCase())
  let lowerCaseArray2 = stringArray2.map(x => x.toLowerCase())

  lowerCaseArray1.sort();
  lowerCaseArray2.sort();

  if (lowerCaseArray1.length !== lowerCaseArray2.length) {
    return false
  }

  for (i = 0; i < lowerCaseArray1.length; i++) {
    if (lowerCaseArray1[i] !== lowerCaseArray2[i]) return false;
  }

  return true;
}

listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

console.log(anagramsFor("threads", listOfWords));

module.exports = anagramsFor;