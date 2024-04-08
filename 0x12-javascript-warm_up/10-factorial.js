#!/usr/bin/node
argv = require('process').argv;
function fact(num)
{
    if (num === 0 || isNaN(num))
    {
        return;
    }
    return num * fact(num - 1)
}
console.log(fact(parseInt(argv[2])))

