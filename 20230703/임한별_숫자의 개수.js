const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n"); 

const str = String(input[0] * input[1] * input[2]);

for (var i = 0; i <= 9; i++) {
    let x = 0;

    for (var j = 0; j < str.length; j++) {
        if (Number(str[j]) == i) {
            x++;
        }
    }
    console.log(x);
}