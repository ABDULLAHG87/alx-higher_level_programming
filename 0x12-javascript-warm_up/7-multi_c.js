#!/usr/bin/node

const argc = Math.floor(Number(process.argv[2]));

if (!isNaN(argc)) {
  for (let n = 0; n < argc; n++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
