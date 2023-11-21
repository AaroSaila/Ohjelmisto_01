'use strict';


const trigger = document.querySelector('#trigger');
const image = document.querySelector('#target');

trigger.addEventListener('mouseenter', function() {
    image.setAttribute('src', 'img/picB.jpg');
})

trigger.addEventListener('mouseleave', function() {
    image.setAttribute('src', 'img/picA.jpg');
})