#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body).results;
    for (const i in res) {
      const chars = res[i].characters;
      for (const j in chars) {
        if (chars[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
