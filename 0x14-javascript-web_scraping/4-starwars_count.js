#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const chars = data.results[0].characters.find(c => c.includes('18'));
  request.get(chars, (err, res, body) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(body).films.length);
  });
});
