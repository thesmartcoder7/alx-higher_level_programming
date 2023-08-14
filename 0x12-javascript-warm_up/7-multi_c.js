#!/usr/bin/node
const first = process.argv[2];
if (first === undefined || isNaN(first)) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < first; i++) {
    console.log("C is fun");
  }
}
