'use strict';

function createLiElement(list_id, text) {
    const li_node = document.createElement('li');
    const text_node = document.createTextNode(text);
    li_node.appendChild(text_node);
    document.getElementById(list_id).appendChild(li_node);
    return;
}


const target = document.querySelector('#target');

createLiElement('target', 'First item');
createLiElement('target', 'Second item');
createLiElement('target', 'Third item');

const li_elements = document.querySelectorAll('li');
li_elements[1].classList.add('my-item');