#!/usr/bin/node
argv = require('process').argv;
function add(a, b)
{
    return a + b;
}
let a = parseInt(argv[2])
let b = parseInt(argv[3])
let x = add(a, b)
console.log(x);