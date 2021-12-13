#!/usr/bin/node
const ARGVCOUNT = 'process.argv.slice(2).length';
if (ARGVCOUNT > 1) {
	console.log('Arguments found');
} else if (ARGVCOUNT === 1) {
	console.log('Argument found');
} else {
	console.log('No argument');
}
