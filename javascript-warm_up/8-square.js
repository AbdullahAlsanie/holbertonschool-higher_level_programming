#!/usr/bin/node
const { argv } = require('process');
if (!Number(argv[2])) {
  console.log('Missing size');
} else {
  const str = 'X';
  str.repeat(Number(argv[2]));
  const repeatNumber = Number(argv[2]);
  for (let i = 0; i < repeatNumber; i++) {
    console.log(str.repeat(repeatNumber));
  }
}
