#!/usr/bin/node
const ARRAY = process.argv;
if (isNaN(ARRAY[2])) {
  console.log('Missing size');
} else {
  const CHAR = 'X'.repeat(parseInt(ARRAY[2]));
  for (let i = 0; i < parseInt(ARRAY[2]); i++) {
    console.log(CHAR);
  }
}
