'use strict';


// Random int between min and max-1
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}


function diceThrow() {
    return getRandomInt(1, 7);
}


function diceThrowSum(dice_amount) {
    let sum = 0;
    let eyes = [];
    for (let i = 0; i <= (dice_amount - 1); i++) {
        let eye = diceThrow();
        eyes[i] = eye;
    }
    for (let i = 0; i < ((dice_amount - 1) / 2); i++) {
        sum += eyes[0] + eyes[1];
        // console.log('Eyes: ' + eyes);
        eyes.splice(0, 2);
        // console.log('Sum: ' + sum);
    }
    return sum;
}

function howManyCorrectSums(dice_amount, sum) {
    let correct_sums = 0;
    for (let i = 0; i <= 10000; i++) {
        const thrown_sum = diceThrowSum(dice_amount);
        if (thrown_sum == sum) {
            correct_sums++
        }
    }
    return correct_sums;
}


const dice_amount = parseInt(prompt('Amount of dice: '));
const sum = parseInt(prompt('Sum of the eye numbers of interest: '));

const correct_sums = howManyCorrectSums(dice_amount, sum);
const probability_in_prcnt = ((correct_sums / 10000) * 100).toFixed(2);

document.querySelector('#probability').innerHTML = `Probability to get sum ${sum} with ${dice_amount} dice is ${probability_in_prcnt}%`;
