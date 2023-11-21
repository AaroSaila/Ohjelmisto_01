'use strict';


const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const operation = document.getElementById('operation');
const button = document.getElementById('start');
const result = document.querySelector('#result');

button.addEventListener('click', function() {
    const num1_value = parseInt(num1.value);
    const num2_value = parseInt(num2.value);
    const operation_value = operation.value;
    if (!isNaN(num1_value) && !isNaN(num2_value)) {
        switch (operation_value) {
            case 'add':
                result.innerHTML = num1_value + num2_value;
                break;
            case 'sub':
                result.innerHTML = num1_value - num2_value;
                break;
            case 'multi':
                result.innerHTML = num1_value * num2_value;
                break;
            case 'div':
                result.innerHTML = num1_value / num2_value;
                break;
    }
    }else {
        result.innerHTML = 'Invalid input';
    }
})