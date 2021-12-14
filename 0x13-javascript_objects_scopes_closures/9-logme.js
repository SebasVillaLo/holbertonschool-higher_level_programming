#!/usr/bin/node
let countitems = 0;
exports.logMe = function (item) {
  console.log(countitems + ': ' + item);
  countitems++;
};
