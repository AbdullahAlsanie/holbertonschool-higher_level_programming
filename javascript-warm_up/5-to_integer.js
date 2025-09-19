#!/usr/bin/node
const { argv } = require('process');
if (Number(argv[2])) {
  console.log(`My number: ${Number(argv[2])}`);
} else {
  console.log('Not a number');
}
