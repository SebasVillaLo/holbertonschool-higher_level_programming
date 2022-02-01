#!/usr/bin/node
const request = require('request');
const argv = process.argv.slice(2);

request(argv[0], function (err, response) {
  if (err) { console.log(err); }
  console.log('code:', response.statusCode);
});
