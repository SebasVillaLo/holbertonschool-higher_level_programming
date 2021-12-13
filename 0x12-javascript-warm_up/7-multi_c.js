#!/usr/bin/node
const ARRAY = process.argv;
if (isNaN(ARRAY[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(ARRAY[2]); i++) {
    console.log('C is fun');
  }
}
