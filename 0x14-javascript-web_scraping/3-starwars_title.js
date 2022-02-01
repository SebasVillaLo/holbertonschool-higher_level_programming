#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2);

request('https://swapi-api.hbtn.io/api/films/' + argv[0], function (err, r, body) {
  if (err) { console.log(err); }
  const string = JSON.parse(body);
  console.log(string.title);
});
