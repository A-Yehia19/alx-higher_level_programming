#!/usr/bin/node

const { argv } = require('node:process');

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }

  return n * factorial(n - 1);
}

const number = parseInt(argv[2]);

console.log(factorial(number));
