#!/usr/bin/node

/**
 * Computes the factorial of a number
 * @function
 * @param{number} num - number to computes it factorial
 */

function factorial(n) {
  let result = 1
  if (n == 0 || isNaN(n)){
    return result;
  } else{
     for (let i = 2; i <= n; i++) {
	result *= i;
     }
      return result;
  }
}

let number = Number(process.argv[2]);
let fact_result = factorial(number);
console.log(fact_result);
