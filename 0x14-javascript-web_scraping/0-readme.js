#!/usr/bin/node
const argv = process.argv.slice(2);
const fs = require('fs');

fs.readFile(argv[0], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
