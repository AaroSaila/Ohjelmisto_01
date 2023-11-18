'use strict';

const participants = [];
const number_of_participants = parseInt(prompt('How many participants?'));

for (let i = 1; i <= number_of_participants; i++) {
    participants.push(prompt('Name of participant ' + i + ':'));
}

participants.sort();

if (participants[0]) {
    for (let i = 0; i < participants.length; i++) {
        document.querySelector('#list').innerHTML += `<li>${participants[i]}</li>`;
    }
}
