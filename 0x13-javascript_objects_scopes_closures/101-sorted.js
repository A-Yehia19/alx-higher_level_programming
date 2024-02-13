#!/usr/bin/node

const dict = require('./101-data').dict;

const ans = {};
for (const key in dict) {
  const value = dict[key];
  if (ans[value] === undefined) {
    ans[value] = [];
  }
  ans[value].push(key);
}

console.log(ans);
