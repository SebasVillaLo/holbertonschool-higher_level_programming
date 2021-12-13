#!/usr/bin/node
const ARRAY = process.argv;
if (isNaN(ARRAY[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(ARRAY[2]));
}
