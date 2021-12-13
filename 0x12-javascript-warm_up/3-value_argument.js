#!/usr/bin/node
const ARRAY = process.argv.slice(2);
if (ARRAY[0] === undefined) {
  console.log('No argument');
} else {
  console.log(ARRAY[0]);
}
