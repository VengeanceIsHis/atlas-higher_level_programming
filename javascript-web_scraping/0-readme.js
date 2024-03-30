#!/usr/bin/nodejs
let reader = FileReader();
const argument = process.argv;
reader.readAsDataURL(argument[2]);