#!/usr/bin/node
const importdic = require('./101-data.js').dict;
const newdict = {};
for (const key in importdic) {
  if (newdict[importdic[key]] === undefined) {
    newdict[importdic[key]] = [];
  }
  newdict[importdic[key]].push(key);
}
console.log(newdict);
