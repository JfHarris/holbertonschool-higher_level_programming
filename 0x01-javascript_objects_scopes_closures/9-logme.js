#!/usr/bin/node
// function prints the # of args already printed and new arg val
exports.logMe = function (item) {
  this.insts = (this.insts || 0) + 1;
  console.log(`${this.insts - 1}: ${item}`);
};
