#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv.slice(2);

request(argv[0], function (err, r, body) {
  if (err) { console.log(err); }
  try {
    fs.writeFileSync(argv[1], body, 'utf8');
    // file written successfully
  } catch (err) {
    console.error(err);
  }
});
