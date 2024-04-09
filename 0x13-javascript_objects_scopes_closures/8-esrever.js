#!/usr/bin/node

function reve(list) {
    let j = list.length -1;
    for (let i = 0; i < (list.length /2); i++ )
    {

        let tmp = list[i];
        list[i] = list[j];
        list[j] = tmp;
        j--;
    }
    return list;
}
exports.esrever = function (list) {
    return reve(list)
}