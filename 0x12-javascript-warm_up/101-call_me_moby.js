#!/usr/bin/node
let callMeMoby = (x, theFunction) => {
    let i = 0;
    while(i != x)
    {
        theFunction();
        i++;
    }
}
module.exports.callMeMoby = callMeMoby