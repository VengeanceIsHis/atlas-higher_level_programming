#!/usr/bin/nodejs
const headerElement = document.querySelector('header');

if (headerElement)
 {
    headerElement.style.color = '#FF0000';
 } else {
    console.error("No element")
 }
