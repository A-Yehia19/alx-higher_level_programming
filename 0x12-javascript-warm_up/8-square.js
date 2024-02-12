#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  let line = '';

  for (let i = 0; i < num; i++) {
    line += 'X';
  }

  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}
