#!/usr/bin/node
let ans;
if (process.argv.length < 1) {
    ans = "No argument";
} else if (process.argv.length === 1) {
    ans = "Argument found";
} else {
    ans = "Arguments found";
}
console.log(ans);
