'use strict';


const numbers = [2, 7, 4];


function even(input_array) {
    let output_array = [];
    for (let i = 0; i <= (input_array.length - 1); i++) {
        if (input_array[i] % 2 == 0) {
            output_array.push(input_array[i]);
        }
    }
    return output_array;
}


const even_numbers = even(numbers);

console.log(`Original array: [${numbers}]`);
console.log(`New array: [${even_numbers}]`);
