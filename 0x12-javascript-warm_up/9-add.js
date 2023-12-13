#!/usr/bin/node

/**
 * add the sum of two numbers
 * @function
 * @param{number} a - first number
 * @param{number} b - second number
 */

function add (a, b) {
  return (a + b);
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  const result = add(num1, num2);
  console.log(result);
}
