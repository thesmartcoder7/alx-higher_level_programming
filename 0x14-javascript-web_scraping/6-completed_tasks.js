#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const list = JSON.parse(body);
    const completed = {};
    list.forEach((item) => {
      if (item.completed && completed[item.userId] === undefined) {
        completed[item.userId] = 1;
      } else if (item.completed) {
        completed[item.userId] += 1;
      }
    });
    console.log(completed);
  }
});
