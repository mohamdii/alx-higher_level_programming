#!/usr/bin/node

const oldSquare = require("./5-square");

class Square extends oldSquare {

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