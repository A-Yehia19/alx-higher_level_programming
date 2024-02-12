#!/usr/bin/node

const numbers = process.argv.slice(2);

if (numbers.length <= 1) {
  console.log(0);
} else {
  numbers.sort((a, b) => parseInt(a) - parseInt(b));
  console.log(numbers[numbers.length - 2]);
}
