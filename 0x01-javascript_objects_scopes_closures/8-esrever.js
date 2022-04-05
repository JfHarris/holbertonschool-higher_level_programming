#!/usr/bin/node
//  function that returns the reversed version of a list
exports.esrever = function (list) {
  const revList = list.slice();
  let x = 0;
  for (x = 0; x < list.length; x++) {
    list[x] = revList[list.length - x - 1];
  }
  return list;
};
