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
    res.json(body);  //this will be the send
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
    res.json(body);  //this will be the send
});

app.get('/append', function(req, res){
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
    res.json(body);  //this will be the send
});

app.listen(8001);