#!/usr/bin/nodejs
if (process.argv[2]) {
    let one = process.argv[2];
}
else {
    let one ="undefined"
}
if (process.argv[3]) {
    let two = process.argv[3];
}
else {
    let two = "undefined"
}
console.log(one, "is", two)
