#!/usr/bin/node

exports.esrever = function (list) {
  let newList = [];
  for (const obj of list) {
    newList.push(obj);
  }
  return newList;
};
