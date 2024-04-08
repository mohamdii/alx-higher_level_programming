#!/usr/bin/node

argv = require('process').argv;

let x, i, row;
row = '';
x = parseInt(argv[2]);
if (isNaN(x))
{
    console.log('Missing number of occurrences')
}
for (i = 0; i < x; i++)
{
    for (let j = 0; j < x; j++)
    {
        row +='X'
    }
    if (i !== x - 1)
    {
        row +='\n'
    }
}
console.log(row)