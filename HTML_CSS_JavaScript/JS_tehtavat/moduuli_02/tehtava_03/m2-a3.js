'use strict';

const dogs = [];

for (let i = 1; i <= 6; i++) {
    dogs.push(prompt(`Dog (${i})`));
}

dogs.sort();
dogs.reverse();

for (let i = 0; i < dogs.length; i++) {
    document.querySelector('#list').innerHTML += `<li>${dogs[i]}</li>`;
}
