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


const year = parseInt(prompt('Enter a year: '))

if (isLeapYear(year)) {
    document.querySelector('#leap-year').innerHTML = `The year ${year} is a leap year`;
}
else {
    document.querySelector('#leap-year').innerHTML = `The year ${year} is not a leap year`;
}
