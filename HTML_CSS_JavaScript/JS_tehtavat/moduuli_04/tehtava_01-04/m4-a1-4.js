'use strict';


const button = document.querySelector('input[type="submit"]');
const text_input = document.getElementById('query');
const form = document.querySelector('form');
const results = document.getElementById('results');


function showShow(show) {
    // article
    const article = document.createElement('article');

    // h2 (name)
    const name = document.createElement('h2');
    const nameContent = document.createTextNode(show['show']['name']);
    name.appendChild(nameContent);

    // a (url)
    const link = document.createElement('a');
    const linkContent = document.createTextNode('Link');
    link.appendChild(linkContent);
    link.setAttribute('href', show['show']['url']);
    link.setAttribute('target', '_blank');

    // img (medium image)
    const img = document.createElement('img');
    img.setAttribute('src', show.show.image.medium != 'null' ? show.show.image.medium : 'https://via.placeholder.com/210x295?text=Not%20Found');
    console.log(show.show.image.medium);
    img.setAttribute('alt', show['show']['name']);
    img.setAttribute('style', 'display="block"');

    // summaryDiv
    const summary = document.createElement('div');
    summary.innerHTML = show.show.summary;

    // Appends to article
    article.appendChild(name);
    article.appendChild(link);
    article.appendChild(img);
    article.appendChild(summary);

    return article;
};



form.addEventListener('submit', async (event) => {
    event.preventDefault();
    results.innerHTML = '';
    const query = form.action + '?q=' + text_input.value;
    console.log(query);
    try {
        const response = await fetch(query);
        const response_json = await response.json();
        console.log(response_json);
        for (let i = 0; i < response_json.length; i++) {
            results.appendChild(showShow(response_json[i]));
        };
    } catch(error) {
        console.error(error);
    };
    
});