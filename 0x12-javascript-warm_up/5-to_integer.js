#!/usr/bin/node

const argv = require("process").argv;
let x;
x = parseInt(argv[2]);
if (isNaN(x))
{
    console.log('Not a number')
}
else
{
    console.log('My number: ' + x)
}