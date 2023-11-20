'use strict';


function createLiElement(list_id, text) {
    const li_node = document.createElement('li');
    const text_node = document.createTextNode(text);
    li_node.appendChild(text_node);
    document.getElementById(list_id).appendChild(li_node);
    return;
}


const names = ['John', 'Paul', 'Jones'];

for (let i = 0; i < names.length; i++) {
    createLiElement('target', names[i]);
}