#!/usr/bin/node

const { argv } = require('node:process');

function add(a, b){
  return a + b;
}

const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

console.log(add(num1, num2));
