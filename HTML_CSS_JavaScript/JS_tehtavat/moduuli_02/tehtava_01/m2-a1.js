'use strict';

const numbers = [];

for (let i = 1; i <= 5; i++) {
    const num = parseInt(prompt(`Input a number (${i}/5): `));
    numbers[i-1] = num;
}

for (let i = 5; i > 0; i--) {
    console.log(numbers[i-1]);
}