#!/usr/bin/node
exports.addMeMaybe = function (inte, theFunc) {
  const x = inte + 1;
  theFunc(x);
};
