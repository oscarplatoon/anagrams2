const sameLengthArrays = require('./sameLengthArrays');
test('will filter out the arrays that have same length', () => {
  const wordOne = "saltier";
  const listWordsOne = ["cognac", "saltier", "realist", "retails", "rainbow", "aaaaaaa"];
  const expectedOutputOne = ["saltier", "realist", "retails","rainbow", "aaaaaaa"];
  ///////////////////////////////////////////////////////////////
  const wordTwo = "aa";
  const listWordsTwo = ["co", "sa", "realist", "re", "rw", "aaa"];
  const expectedOutputTwo = ["co", "sa", "re","rw"];
  ///////////////////////////////////////////////////////////////
  const wordThree = "tier";
  const listWordsThree = ["gnac","kimchi","tier", "list", "tails", "rain","aaaaaa"];
  const expectedOutputThree = ["gnac","tier","list","rain"];
  ///////////////////////////////////////////////////////////////
  
  expect(sameLengthArrays(wordOne,listWordsOne)).toEqual(expectedOutputOne);
  expect(sameLengthArrays(wordTwo,listWordsTwo)).toEqual(expectedOutputTwo);
  expect(sameLengthArrays(wordThree,listWordsThree)).toEqual(expectedOutputThree);
})