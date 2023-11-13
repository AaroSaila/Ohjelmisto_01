'use strict';


function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}


const amount = prompt('How many dice?');
let sum = 0;

for (let i = 1; i <= amount ; i++) {
    const die = getRandomInt(1, 7);
    sum += die;
}

document.querySelector('#sum').innerHTML = `Sum: ${sum}`
