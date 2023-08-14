#!/usr/bin/node

const one = parseInt(process.argv[2]);
const two = parseInt(process.argv[3]);

const add = (a, b) => {
  console.log(a + b);
};

add(one, two);
