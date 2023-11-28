'use strict';


const button = document.querySelector('input[type="submit"]');
const text_input = document.getElementById('query');
const form = document.querySelector('form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const query = form.action + '?q=' + text_input.value;
    console.log(query);
    try {
        const response = await fetch(query);
        const response_json = await response.json();
        console.log(response_json);
    } catch(error) {
        console.error(error);
    };
});