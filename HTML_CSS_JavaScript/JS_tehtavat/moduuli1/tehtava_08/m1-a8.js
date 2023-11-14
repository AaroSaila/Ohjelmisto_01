'use strict';


function isLeapYear(year) {
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0) {
                return true;
            }
            else {
                return false;
            }
        }
        else {
            return true;
        }
    }
    else {
        return false;
    }
}


function createNumberList(first, last, element) {
    const list_element = document.querySelector(element);
    for (first; first <= last; first++) {
        if (isLeapYear(first)) {
            list_element.innerHTML += `<li>${first}</li>`;
        }
    }
    
}


const first = parseInt(prompt('Starting Year'));
const last = parseInt(prompt('Last Year'));
document.querySelector('#text').innerHTML = `Leap years between years ${first} and ${last}:`
createNumberList(first, last, '#year');