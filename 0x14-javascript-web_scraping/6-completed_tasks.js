#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const obj = {};
  JSON.parse(body).map(todo => {
    obj[todo.userId] = (obj[todo.userId] || 0) + (todo.completed ? 1 : 0);
    return obj;
  });
  console.log(obj);
});
