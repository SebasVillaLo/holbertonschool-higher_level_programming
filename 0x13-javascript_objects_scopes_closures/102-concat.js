#!/usr/bin/node
const argument = process.argv.slice(2);
const fs = require('fs');
const fileone = fs.readFileSync('./' + argument[0]);
const filesecond = fs.readFileSync('./' + argument[1]);
fs.writeFileSync('./' + argument[2], fileone + filesecond);
