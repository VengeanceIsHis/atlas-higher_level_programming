#!/usr/bin/nodejs
const reader = FileReader();
const argument = process.argv;
reader.readAsDataURL(argument[2]);