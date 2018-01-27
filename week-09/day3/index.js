'use strict';

const express = require('express');

const app = express();

app.use('/assets', express.static('assets'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', function(req, res){
    let body;
    if (req.query.input === undefined) {
        body = {
            "error": 'Please provide an input!'
        }   
    } else {
        body = {
            "received": req.query.input,
            "result": req.query.input * 2
        }
    }
    res.json(body);  
});

app.get('/greeter', function(req, res){
    let body;
    if (req.query.name === undefined) {
        body = {
            "error": 'Please provide a name!'
        }   
    } else if (req.query.title === undefined) {
        body = {
            "error": 'Please provide a title!'
        }   
    } else {
        body = {
            "welcome_message": "Oh, hi there " + req.query.name + " my dear " + req.query.title + " !"
        }
    }
    res.json(body);  
});

app.get('/appenda/:appendable', function(req, res){
    let body;
    if (req.params != null) {
        body = {
            "appended": req.params.appendable + "a"
        }
        res.json(body);
    } else {
        res.status(404);
    }
});

app.post('/dountil/:what', function (req, res) {
    let body;
    if (req.params.what != null) {
      if (req.params.what === 'sum') {
        let sum = 0;
        for (let i = 1; i <= req.body.until; i++ ) {
          sum += i;
        }
        body = {
          "result": sum
        }
      } else if (req.params.what === 'factor') {
        let factor = 0;
        for (let i = 1; i <= req.body.until; i++ ) {
          factor *= i;
        }
        body = {
          "result": factor
      }
      }
    } else {
      body = {
          "error": "Please provide a number!"
      }
    }
    res.json(body);
  });

app.listen(8080);