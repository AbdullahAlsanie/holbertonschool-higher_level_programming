#!/usr/bin/node
const { argv } = require('process');
if (!argv[2] || !argv[3]) {
  console.log(0);
} else if (Number(argv[2]) === 1 && !argv[3]) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < argv.length; i++) {
    arr.push(argv[i]);
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
