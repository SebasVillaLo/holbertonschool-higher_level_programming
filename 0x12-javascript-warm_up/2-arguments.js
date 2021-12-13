#!/usr/bin/node
const no = 'No argument';
const si = 'Arguments found';
if (process.argv.slice(2).length === 0) {
	console.log(no);
} else if (process.argv.slice(2).length === 1) {
	console.log(si);
} else {
	console.log(si);
}