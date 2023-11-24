'use strict';


const calculation = document.querySelector('#calculation');
const button = document.querySelector('#start');
const result = document.querySelector('#result');


function whatOperator(string) {
    const operators = ['+', '-', '*', '/'];
    const included_operators = [];
    for (let i = 0; i < operators.length; i++) {
        if (string.includes(operators[i])) {
            included_operators.push(operators[i])
        }
    }
    if (included_operators.length == 1) {
        return included_operators[0];
    }
    else {
        return 'Invalid Input';
    }
}


function calculationFn(string) {
    let result;
    const operator = whatOperator(string);
    if (operator == 'Invalid Input') {
        return 'Invalid Input';
    }
    const numbersStr = string.split(operator);
    switch (numbersStr.length) {
        case 2:
            const numbersInt = [];
            for (let i = 0; i < numbersStr.length; i++) {
                numbersInt.push(parseInt(numbersStr[i]));
            }
            switch (operator) {
                case '+':
                    result = numbersInt.reduce((a, b) => a+b);
                    break;
                case '-':
                    result = numbersInt.reduce((a, b) => a-b);
                    break;
                case '*':
                    result = numbersInt.reduce((a, b) => a*b);
                    break;
                case '/':
                    result = numbersInt.reduce((a, b) => a/b);
                    break;
            }
            break;
        default:
            result = 'Invalid Input';
            break;
    }
    
    return result;
}


button.addEventListener('click', function() {
    let calculationResult = calculationFn(calculation.value);
    result.innerHTML = calculationResult;
    return;
});
