#!/usr/bin/node
let arg = process.argv[2];
if (isNaN(arg)) {
    console.log('Missing size');
} else {
    for (let i=0; i< parseInt(arg); i++)
        console.log('X'.repeat(parseInt(arg)))
}
