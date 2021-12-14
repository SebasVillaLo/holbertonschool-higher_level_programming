#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    if (c === 'C') {
      console.log(('C'.repeat(this.width) + '\n').repeat(this.height - 1) + 'C'.repeat(this.width));
    } else {
      console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
    }
  }
};
