#!/usr/bin/node

/**
 * Computes the factorial of a number
 * @function
 * @param{number} num - number to computes it factorial
 */

function factorial (n) {
  let result = 1;
  if (n === 0 || isNaN(n)) {
    return result;
  } else {
    for (let i = 2; i <= n; i++) {
      result *= i;
    }
    return result;
  }
}

const number = Number(process.argv[2]);
const factResult = factorial(number);
console.log(factResult);
