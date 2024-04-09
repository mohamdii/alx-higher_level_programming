#!/usr/bin/node

const  argv  = require("process").argv;

if (argv.length < 2)
{
    console.log(0);
}
let dif = 0;
let biggest = argv[2]
let second = argv[2]
for (let i = 2; i < argv.length; i++)
{
    if (biggest < argv[i])
    {
        biggest = argv[i]
    }
}
for (i = 2; i < argv.length; i++)
{
    if (argv[i] == biggest)
    {
        continue;
    }
    if (second < argv[i])
    {
        second = argv[i]
    }
}
console.log(second)