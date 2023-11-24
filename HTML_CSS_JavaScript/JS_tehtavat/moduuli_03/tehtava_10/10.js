'use strict';


const button = document.querySelector('input[type="submit"]');
const firstName = document.querySelector('input[name="firstname"]');
const lastName = document.querySelector('input[name="lastname"]');
const text = document.querySelector('#target');

button.addEventListener('click', function(event) {
    event.preventDefault();
    text.innerHTML = `Your name is ${firstName.value} ${lastName.value}`;
    return;
})
