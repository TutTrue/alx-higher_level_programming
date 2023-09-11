#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) { console.log(0); } else {
  let max = process.argv[2];
  let second = process.argv[3];
  process.argv.forEach(el => {
    if (el > max) { max = el; }
    if (el > second && el !== max) { second = el; }
  });
  console.log(second);
}
