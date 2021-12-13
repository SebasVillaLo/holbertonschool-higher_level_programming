#!/usr/bin/node
const ARRAY = process.argv.slice(2).map(Number);
if (ARRAY[0] === undefined) {
  console.log(0);
} else if (ARRAY.length === 1) {
  console.log(0);
} else {
  const second = ARRAY.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
