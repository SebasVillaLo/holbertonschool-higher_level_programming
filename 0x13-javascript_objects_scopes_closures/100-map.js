#!/usr/bin/node
const listanew = require('./100-data').list;
let indice = 0;
const map = listanew.map(x => x * indice++);
console.log(listanew);
console.log(map);
