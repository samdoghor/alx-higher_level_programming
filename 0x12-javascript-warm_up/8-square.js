#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const line = 'X';
  let i = 0;

  while (i < process.argv[2]) {
    console.log(line.repeat(process.argv[2]));
    i += 1;
  }
}
