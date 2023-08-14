#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const ex = 'X'.repeat(size);
  for (let row = 0; row < size; row++) {
    console.log(ex);
  }
}
