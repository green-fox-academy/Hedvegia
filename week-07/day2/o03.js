'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

var args = process.argv.splice(2);
console.log('Input params are', args);

var from = parseFloat(args[0], 10)
var to = parseFloat(args[1], 10)
var amount = parseFloat(args[2], 10)


function checkFrom(list) {
    var checkF = 0
    list.forEach(function(item) {
        if (from == item.account_number) {
            item.balance -= amount
            checkF += 1
            console.log('From ' + item.client_name)
        } 
    });
    return checkF
}

function checkTo(list) {
    var checkT = 0
    list.forEach(function(item) {
        if(to == item.account_number) {
            item.balance += amount
            console.log('To ' + item.client_name)
            checkT += 1
        } 
    });
    return checkT
}

function transfer(account) {
    if (checkFrom(account) == 1 && checkTo(account) == 1) {
        console.log(accounts)
    } else {
        console.log('404 - account not found')
    }
}

transfer(accounts);