'use strict';

var getData = function() {

    let httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', 'http://secure-reddit.herokuapp.com/simple/posts', true); 
    httpRequest.send(null);

    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {
            let data = JSON.parse(httpRequest.responseText).posts
            console.log(data);

            data.forEach(function(element) {
                let body = document.querySelector('body')
                let mainContentDiv = document.createElement('div');
                mainContentDiv.setAttribute('class', 'main-content');
                body.appendChild(mainContentDiv);

                let arrowsDiv = document.createElement('div');
                arrowsDiv.setAttribute('class', 'arrows')
                mainContentDiv.appendChild(arrowsDiv);

                let upArrowImg = document.createElement('img');
                upArrowImg.setAttribute('src', 'upvote.png');
                arrowsDiv.appendChild(upArrowImg);

                let scoreParagraph = document.createElement('p');
                scoreParagraph.textContent = element.score;
                arrowsDiv.appendChild(scoreParagraph);

                let downArrowImg = document.createElement('img');
                downArrowImg.setAttribute('src', 'downvote.png');
                arrowsDiv.appendChild(downArrowImg);

                let textContentDiv = document.createElement('div');
                textContentDiv.setAttribute('class', 'text-content');
                mainContentDiv.appendChild(textContentDiv);

                let titleHeader = document.createElement('h2');
                titleHeader.textContent = element.title;
                textContentDiv.appendChild(titleHeader);

                let urlP = document.createElement('p');
                urlP.textContent = element.url;
                textContentDiv.appendChild(urlP);

                let modifyAnchor = document.createElement('a');
                modifyAnchor.setAttribute('class', 'modify');
                textContentDiv.appendChild(modifyAnchor);

                let deleteAnchor = document.createElement('a');
                deleteAnchor.setAttribute('class', 'delete');
                textContentDiv.appendChild(deleteAnchor);
            });
        }
    }
}

getData();