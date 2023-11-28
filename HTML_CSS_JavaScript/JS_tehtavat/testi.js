'use strict';


function success(position) {
    console.log(position);
    return;
}

function error(failure) {
    console.log(failure);
    return;
}


navigator.geolocation.getCurrentPosition(success, error, {enableHighAccuracy: true});
