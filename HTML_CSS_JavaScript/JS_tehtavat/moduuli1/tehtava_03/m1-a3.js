'use strict';

const num1 = parseInt(prompt('Input a number'));
const num2 = parseInt(prompt('Input a number'));
const num3 = parseInt(prompt('Input a number'));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.querySelector('#sum').innerHTML = `Sum: ${num1} + ${num2} + ${num3} = ${sum}`;
document.querySelector('#product').innerHTML = `Product: ${num1} * ${num2} * ${num3} = ${product}`;
document.querySelector('#average').innerHTML = `Average: (${num1} + ${num2} + ${num3}) / 3 = ${average}`;
