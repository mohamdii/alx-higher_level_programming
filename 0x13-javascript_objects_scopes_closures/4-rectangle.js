#!/usr/bin/node

class Rectangle {
    constructor(w, h){
        if (w > 0 && h > 0)
        {
            this.width = w;
            this.height = h;
        }
    }
    print() {
        let x = '';
        for (let i = 0; i < this.height; i++)
        {
            for (let j = 0; j < this.width; j++)
            {
                x += 'X'
            }
            if (i < this.height -1)
            {
                x += '\n'
            }
        }
        console.log(x)
    }
    rotate() {
        let tmp = this.height;
        this.height = this.width;
        this.width = tmp;
    }
    double() {
        this.width = 2 * this.width;
        this.height = 2 * this.height;
    }
}
module.exports = Rectangle;