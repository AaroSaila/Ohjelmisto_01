'use script';


let result;


// Returns an integer between min and max (both included) [w3schools.com]
/* function randomInt(min, max) {
    return Math.floor(Math.random() + (max - min + 1)) + min;
} */


function dieRoll() {
    return Math.floor(Math.random() + (6 - 1 + 1)) + 1;
}


/* while (result != 6) {
    result = dieRoll();
    console.log(result);
    if (result != 0) {
        document.querySelector('#list').innerHTML += `<li>${result}</li>`;
    }
} */