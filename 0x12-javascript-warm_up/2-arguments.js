#!/usr/bin/node

const argv = require('process').argv;

argv.forEach((val, index) => {
    if (index > 1 ) {
        console.log('Arguments found');
    } else {
        console.log('No argument');
    }
});