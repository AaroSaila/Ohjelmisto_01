'use strict';


function createOptionElement(element_id, attribute_value, text) {
  // Creates node (the element to be inserted)
  const node = document.createElement('option');
  // Creates the text inside the node
  const text_node = document.createTextNode(text);
  // Appends the the text inside of the above created element
  node.appendChild(text_node);
  // Sets the value attribute of the above created element
  node.setAttribute('value', attribute_value);
  // Inserts the above created and modified element below the element referred by element_id
  document.getElementById(element_id).appendChild(node);
  return;
}


const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

for (let i = 0; i < students.length; i++) {
  createOptionElement('target', students[i]['id'], students[i]['name']);
}
