#!/usr/bin/nodejs
let reader = new FileReader();
const argument = process.argv;
reader.readAsDataURL(argument[2]);