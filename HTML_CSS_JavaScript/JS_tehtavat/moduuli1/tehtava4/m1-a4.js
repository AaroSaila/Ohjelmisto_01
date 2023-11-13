'use strict';

// Returns random integer between min and max-1.
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

let house;
const house_num = getRandomInt(1, 5);

if (house_num == 1) {
    house = 'Gryffindor';
}
else if (house_num == 2) {
    house = 'Slytherin';
}
else if (house_num == 3) {
    house = 'Hufflepuff';
}   
else if (house_num == 4) {
    house = 'Ravenclaw';
}
else {
    console.log('else ifs not working')
}
console.log(house_num, house);

const name = prompt('Input your name: ');

document.querySelector('#house-text').innerHTML = `${name}, you are ${house}.`;
