#!/usr/bin/nodejs
const args = process.argv;
let param = args[2];
let i = 0, j = 0;
let string = "";
if (parseInt(param))
{
    while (i < param)
    {
        let temp_string = "";
        while (j < param)
        { 
            temp_string += 'X';
            j++;
        }
        string = temp_string;
        console.log(string);
        i++;
    }
}