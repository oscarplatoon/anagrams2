// Can you translate this driver code to unit tests?

const anagramsFor = require('./anagram2')

var listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"]

test('properly return list of true anagrams', () => {
  expect(anagramsFor('threads', listOfWords)).toEqual(['threads','trashed','hardest','hatreds'])
})

test('properly return empty list', () => {
  expect(anagramsFor('apple', listOfWords)).toEqual([])
})


// var ana = require("./anagram2"),
// listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

// console.log(ana.anagramsFor("threads", listOfWords).length == 4);
// console.log(ana.anagramsFor("threads", listOfWords)[0] == "threads");
// console.log(ana.anagramsFor("threads", listOfWords)[1] == "trashed");
// console.log(ana.anagramsFor("threads", listOfWords)[2] == "hardest");
// console.log(ana.anagramsFor("threads", listOfWords)[3] == "hatreds");

// console.log(ana.anagramsFor("apple", listOfWords).length == 0);
