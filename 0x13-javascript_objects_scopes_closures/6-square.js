#!/usr/bin/node

const Rectangle = require("./4-rectangle");

class Square extends Rectangle {
    constructor(size) {
        super(size, size);
        this.size = size;
    }
    charPrint(c) {
        if (c == undefined)
        {
            c = 'X'
        }
        let p = '';
        for(let i = 0; i < this.size; i++) {
            for (let j = 0; j < this.size; j++) {
                p += c;
            }
            if (i < this.size - 1)
            {
                p += '\n'
            }

        }
        console.log(p)    
    }
}
module.exports = Square;