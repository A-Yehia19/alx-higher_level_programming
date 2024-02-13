#!/usr/bin/node

const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    let x = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      x += c;
    }

    for (let j = 0; j < this.height; j++) {
      console.log(x);
    }
  }
};

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');