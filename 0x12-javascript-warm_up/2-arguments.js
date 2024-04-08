#!/usr/bin/node

const argv = require('process').argv;

if (argv != null)
{
    console.log('Argument found');
}
else
{
    console.log('No argument');
}