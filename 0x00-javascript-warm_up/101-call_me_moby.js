#!/usr/bin/node
exports.callMeMoby = function (x, theFunc) {
  let y = x;
  for (y = x; y > 0; y--) {
    theFunc();
  };
};
