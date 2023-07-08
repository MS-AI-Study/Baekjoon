var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().trim();
var n = Number(input);

if (((n % 4 == 0) && (n%100 != 0)) || (n % 400 ==0)){
    console.log(1)
} else {
    console.log(0)
}