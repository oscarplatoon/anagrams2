const anagram = require('./anagram');
test('will return arrays of anagram', () => {
  expect(anagram("saltier", ["cognac", "saltier", "realist", "retails"])).toEqual(["saltier", "realist", "retails"]);
})