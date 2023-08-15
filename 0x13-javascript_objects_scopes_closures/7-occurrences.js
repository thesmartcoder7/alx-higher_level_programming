#!/usr/bin/node
exports.nbOccurences = function (list, term) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === term) {
      count++;
    }
  }
  return count;
};
