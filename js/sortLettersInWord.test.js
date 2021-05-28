const sortedLettersWords = require('./sortLettersInWord');
test('will return words of array in sorted manner', () => {
  const testOne = ["cognac", "saltier", "realist", "retails"];
  const expectedOutput = [ 'accgno', 'aeilrst', 'aeilrst', 'aeilrst' ];
  expect(sortedLettersWords(testOne)).toEqual(expectedOutput);
})