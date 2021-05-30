const ana = require("./anagram2");

test("Threads", () => {
  expect(ana("threads", ["threads", "trashed", "hardest", "hatreds", "hounds"]))===(["threads", "trashed", "hardest", "hatreds"]);
});

test("apple", () => {
  expect(ana("apple", ["threads", "trashed", "hardest", "hatreds", "hounds"])===([]));
});
