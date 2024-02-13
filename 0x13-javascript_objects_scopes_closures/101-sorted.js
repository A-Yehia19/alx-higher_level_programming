#!/usr/bin/node

const dict = require('./100-data').dict;

let ans = {};
for (let key in dict) {
    const value = dict[key];
    if (ans[value] === undefined) {
        ans[value] = [];
    }
    ans[value].push(key);
}

console.log(ans);
