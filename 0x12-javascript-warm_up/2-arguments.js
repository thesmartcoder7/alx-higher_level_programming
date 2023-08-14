#!/usr/bin/node
const totalArguments = process.argv.length - 2;
if (totalArguments === 0) {
  console.log('No argument');
} else if (totalArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
