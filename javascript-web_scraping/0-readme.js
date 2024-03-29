#!/usr/bin/nodejs
var args = process.argv.splice(2,process.argv.length-1);

args.forEach(function (file){
        if(args.length >1)
                console.log(‘========> %s <=========’,file);
        require(‘fs’).readFile(file, function(err,buf){
                process.stdout.write(buf);
        });
});