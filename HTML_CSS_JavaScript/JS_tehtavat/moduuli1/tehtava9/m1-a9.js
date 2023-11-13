'use strict';


function isPrime(number) {
    if (number == 2) {
        return true;
    }
    for (let i = 2; i < number; i++) {
        if (number > 1 && number % i == 0) {
            return false;
        }
        else {
            return true;
        }
    }
}


const num = parseInt(prompt("Input a number to check if it's a prime."));

if (isPrime(num)) {
    document.querySelector('#prime').innerHTML = `${num} is a prime number.`;
}
else {
    document.querySelector('#prime').innerHTML = `${num} is not a prime number.`;
}