'use strict';


const jokesDiv = document.getElementById('jokes');
const search = document.querySelector('input[type="submit"]');
const text_input = document.getElementById('text_input');


async function fetchJoke() {
    try {
        const joke = await fetch('https://api.chucknorris.io/jokes/random');
        const joke_json = await joke.json();
        console.log(joke_json.value);
    }
    catch(error) {
        console.error(error);
    };
};


function createArticle(div, textContent) {
    // article
    const article = document.createElement('article');

    // p
    const p = document.createElement('p');
    const pContent = document.createTextNode(textContent);
    p.appendChild(pContent);

    // Append to article
    article.appendChild(p);

    return article;
};


fetchJoke();

search.addEventListener('click', async (event) => {
    event.preventDefault();
    try {
        const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${text_input.value}`);
        const response_json = await response.json();
        console.log(response_json);
        jokesDiv.appendChild(createArticle(jokesDiv, response_json['result'][0]['value']));
    }
    catch(error) {
        console.error(error);
    };
});