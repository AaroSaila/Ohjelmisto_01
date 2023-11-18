'use strict';

const numbers = [];

while (true) {
    let number = parseInt(prompt('Give a number: '));

    while (isNaN(number)) {
        number = parseInt(prompt('Give a number: '));
    }

    if (numbers.includes(number)) {
        alert('Number already entered.');
        break;
    }
    else {
        numbers.push(number);
    }
}

numbers.sort((a, b) => a - b);

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}
