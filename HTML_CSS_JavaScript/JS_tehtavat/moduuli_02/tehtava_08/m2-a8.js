'use strict';


function concat(input_array) {
    let output_text = '';
    for (let i = 0; i <= (input_array.length - 1); i++) {
        output_text += input_array[i];
    }
    return output_text;
}


const names = ['Arto', 'Bertel', 'Carol', 'Dean'];

document.querySelector('#text').innerHTML = concat(names);