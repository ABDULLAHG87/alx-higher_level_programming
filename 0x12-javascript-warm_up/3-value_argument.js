#!/usr/bin/node

argType = typeof (process.argv[2]);

if (argType === 'undefined') {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
