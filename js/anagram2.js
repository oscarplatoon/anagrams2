const anagramFor = (word, array) => {
  answer = [];
  
  word_array = (word.split('').sort());

  for (let i = 0; i < array.length; i++) {
    if(array[i].split('').sort() === word_array) {
      answer.push(array[i]);
      console.log(answer);
    }
  }
	
  return(answer)
  
};

module.exports = anagramFor


