'use strict';

const sqrt_element = document.querySelector('#square-root');
const answer = confirm('Should I calculate the square root?');

if (answer) {
    const num = parseInt(prompt('Input a number: '));
    if (num > 0) {
        const sqrt = Math.sqrt(num);
        sqrt_element.innerHTML = `The square root of ${num} is ${sqrt}`;
    }
    else {
        sqrt_element.innerHTML = 'The square root of a negative number is not defined'
    }
}
else {
    sqrt_element.innerHTML = 'The square root is not calculated.'
}
