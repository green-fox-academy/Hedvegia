'use strict';

let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=c27533e6a5124cd5ab80351532fd0ddd&q=apollo11', true); // Also try http://444.hu/feed
httpRequest.send(null);

httpRequest.onload = function() {
    if (httpRequest.status >= 200 && httpRequest.status < 400) {
        let text = JSON.parse(httpRequest.responseText);
        let articles = text.response.docs;
        console.log(articles);
        articles.forEach(function(element) {
            let article = document.createElement('h1');
            article.textContent = element.headline.main;
            document.body.appendChild(article);
    
            let snippet = document.createElement('div');
            snippet.textContent = element.snippet;
            document.body.appendChild(snippet);
    
            let date = document.createElement('p');
            date.textContent = element.pub_date;
            document.body.appendChild(date);
    
            let link = document.createElement('a');
            link.textContent = 'more about this topic, here';
            link.setAttribute('href', element.web_url);
            document.body.appendChild(link);
        });
    } else {
        console.log('error');
    }
  };