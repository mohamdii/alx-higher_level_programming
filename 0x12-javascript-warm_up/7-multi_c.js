#!/usr/bin/node

argv = require('process').argv
let x, i;
x = parseInt(argv[2]);
if (isNaN(x))
{
    console.log('Missing number of occurrences')
}

for (i = 0; i < x; i++)
{
    console.log('C is fun')
}