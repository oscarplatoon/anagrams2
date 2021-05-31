const cm = require('./characterMatch') 

exports.anagramsFor = function(word, listOfWords) {

  let outputResult = [];
  if(listOfWords === undefined) {
    return outputResult
  }
  for(let i = 0; i < listOfWords.length; i++) {
    if (cm.isCharacterMatch(word, listOfWords[i])) {
      outputResult.push(listOfWords[i])
    }
  }
  return outputResult;
};
