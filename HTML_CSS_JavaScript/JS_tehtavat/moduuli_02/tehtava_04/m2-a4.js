'use strict';

const numbers = [];

while (true) {
    const number = parseInt(prompt('Give a number (0 to cancel): '));
    if (number == 0) {
        break;
    }
    else {
        numbers.push(number);
    }
}

numbers.sort((a, b) => b - a);

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}