'use strict';


let result;


// Returns an integer between min and max (both included) [w3schools.com]
function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}


function rollDie(sides) {
    return randomInt(1, sides);
}


let sides = 0;
while (sides <= 0) {
    sides = parseInt(prompt('Give the amount of sides of the die: '));
}

while (result != sides) {
    result = rollDie(sides);
    document.querySelector('#list').innerHTML += `<li>${result}</li>`;
}