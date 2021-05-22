const anagramsFor = require('./anagram2');

listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

test('case 1', () => {
  expect(anagramsFor("threads", listOfWords).length).toBe(4);
})

test('case 2', () => {
  expect(anagramsFor("threads", listOfWords)[0]).toEqual("threads");
})

test('case 3', () => {
  expect(anagramsFor("threads", listOfWords)[1]).toEqual("trashed");
})

test('case 4', () => {
  expect(anagramsFor("threads", listOfWords)[2]).toEqual("hardest");
})

test('case 5', () => {
  expect(anagramsFor("threads", listOfWords)[3]).toBe("hatreds");
})

test('case 6', () => {
  expect(anagramsFor("apple", listOfWords).length).toBe(0);
})