#!/usr/bin/node

/**
 * A script that searches the second biggest integer in the list
 * @fileoverview
 */

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2)
    .map(Number)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
