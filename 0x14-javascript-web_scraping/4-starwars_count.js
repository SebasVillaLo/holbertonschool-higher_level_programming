#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/people/18/';
let count = 0;
request(argv[0], function (err, r, body) {
  if (err) { console.log(err); }
  const string = JSON.parse(body);
  const rests = string.results;
  for (const i of rests) {
    for (const j in i.characters) {
      if (i.characters[j] === url) {
        count += 1;
      }
    }
  }
  console.log(count);
});
