#!/usr/bin/node
exports.addMeMaybe = function (number, thefunction) {
  for (let iter = 0; iter < number; iter++) {
    number++;
    thefunction(number);
  }
};
