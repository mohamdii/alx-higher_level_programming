#!/usr/bin/node
const argv = require('process').argv;
console.log(argv[1])
console.log(argv[0])
if (argv.length === 3)
{
    console.log('Argument found');
}
else if (argv.length > 3)
{
    console.log('Arguments found');
}
else
{
    console.log('No argument');
}