#!/usr/bin/node
const argv = process.argv.slice(2);
const fs = require('fs');

try {
  fs.writeFileSync(argv[0], argv[1], 'utf8');
  // file written successfully
} catch (err) {
  console.error(err);
}
