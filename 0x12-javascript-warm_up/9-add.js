#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const FIRTS = parseInt(process.argv[2]);
const SECOND = parseInt(process.argv[3]);
console.log(add(FIRTS, SECOND));
