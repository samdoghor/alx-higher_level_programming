#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;

  let i = 0;

  while (i < list.length) {
    if (searchElement === list[i]) {
      nOccurrences += 1;
    }
    i += 1;
  }
  return nOccurrences;
};
