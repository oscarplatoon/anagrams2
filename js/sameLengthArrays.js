const sameLengthArrays = (word, words) => {
  let wordLength = word.length;
  let result = [];
  for (let i = 0; i < words.length; i++) {
    if(words[i].length === wordLength) {
      result.push(words[i]);
    }
  }
  return result;
}
module.exports = sameLengthArrays;