const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n"); 

x = false;
y = false;
if (input[0] > 0) {
    x = true;
};
if (input[1] > 0) {
    y = true;
};

if (x && y) {
    console.log(1);
}else if (x && y != true) {
    console.log(4);
}else if (x != true && y) {
    console.log(2);
}else { console.log(3);};
