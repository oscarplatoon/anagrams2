const { expect, test} = require('@jest/globals');
const ana = require('./anagram2');

let listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"]
let listOfNumbers = ["3141", "1432", "1743", "31415"]

test('Is it an array?', () => {
  expect(typeof(ana.anagramsFor("test", listOfWords)))
  .toBe(typeof(listOfNumbers))
})

test('Does it correctly evaluate anagrams?', () => {
  expect(ana.anagramsFor("threads", listOfWords).length == 4);
  expect(ana.anagramsFor("threads", listOfWords)[0] == "threads");
  expect(ana.anagramsFor("threads", listOfWords)[1] == "trashed");
  expect(ana.anagramsFor("threads", listOfWords)[2] == "hardest");
  expect(ana.anagramsFor("threads", listOfWords)[3] == "hatreds");
  expect(ana.anagramsFor("apple", listOfWords).length == 0);
})