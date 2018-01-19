'use strict';

let xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", 'http://api.giphy.com/v1/gifs/search?q=cat&api_key=YlfgPQXQ8t4eEBiyLP5qrUgelxT8JPx7&limit=16', true );
xmlHttp.send(null);

xmlHttp.onload = function() {
    let response = JSON.parse(xmlHttp.responseText);
    console.log(response);

    let ul = document.getElementsByTagName('ul')[0];
    
    for (let i = 0; i < response.data.length; i++) {
        let image = document.createElement('img');
        image.setAttribute('src', response.data[i].images.fixed_width_still.url);
        ul.appendChild(image);
        image.addEventListener('click', function() {
        image.setAttribute('src', response.data[i].images.preview_gif.url);
    });
    }
}
