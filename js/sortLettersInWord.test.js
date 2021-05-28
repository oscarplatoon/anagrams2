const sortedLettersWords = require('./sortLettersInWord');
test('will return words of array in sorted manner', () => {
  const testOne = ["cognac", "saltier", "realist", "retails"];
  const expectedOutput = [ 'a,c,c,g,n,o', 'a,e,i,l,r,s,t', 'a,e,i,l,r,s,t', 'a,e,i,l,r,s,t' ];
  expect(sortedLettersWords(testOne)).toEqual(expectedOutput);
})