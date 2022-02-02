#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[0];
request(url, function (err, r, body) {
  if (err) { console.log(err); }
  const string = JSON.parse(body).characters;
  for (const j of string) {
    request(j, function (err, res, body) {
      if (err) { console.log(err); }
      const people = JSON.parse(body);
      console.log(people.name);
    });
  }
});
