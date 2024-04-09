#!/usr/bin/node
let c = -1;
function logMe(item) {
    c++;
    console.log(c + ': ' + item)
}
exports.logMe = function (item) {
    return logMe(item)
}