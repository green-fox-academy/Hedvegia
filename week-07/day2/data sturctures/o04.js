'use strict';

var watchlist = []

var security_alchol_loot = 0

var queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

// Queue of festivalgoers at entry
// no. of alcohol units 
// no. of guns

// Create a security_check function that returns a list of festivalgoers who can enter the festival

// If guns are found, remove them and put them on the watchlist (only the names)
// If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

function securityCheck(list) {
    var whoCanGoes = []
    list.forEach(function(item){
        if (item.alcohol == 0 && item.guns == 0) {
            whoCanGoes.push(item.name);
        }
    });
    console.log(whoCanGoes);
}

securityCheck(queue);

function takeOfGuns(list) {
    list.forEach(function(item) {
        if (item.guns != 0) {
            watchlist.push(item.name);
            item.guns -= 1
        }
    });
    console.log(watchlist)
}

takeOfGuns(queue);

function alcoholLoot(list) {
    list.forEach(function(item) {
        if (item.alcohol != 0) {
            security_alchol_loot += item.alcohol;
            item.alcohol = 0;
        }
    });
    console.log(security_alchol_loot);
}

alcoholLoot(queue);
securityCheck(queue);