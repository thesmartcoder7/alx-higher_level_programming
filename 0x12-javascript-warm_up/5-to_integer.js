#!/usr/bin/node
const first = process.argv[2];
if (first === undefined) {
  console.log("Not a number");
} else if (isNaN(first)) {
  console.log("Not a number");
} else {
  console.log("My number: " + parseInt(first));
}
