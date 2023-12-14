#!/usr/bin/node

module.exports = class Square extends require('./5-square.js') {
  charPrint (z) {
    if (z === undefined) {
      this.print();
    } else {
      for (let n = 0; n < this.height; n++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
};
