# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival



queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

def security_check (queue):
    for i in range(0, len(queue)):
        if queue[i]['guns'] == 0 and queue[i]['alcohol'] == 0:
            go.append(queue[i]['name'])
go =[]
security_check(queue)
print(go)

# If guns are found, remove them and put them on the watchlist (only the names)

def watchls (ls):
	for i in range(0, len(queue)):
		if queue[i]['guns'] != 0:
			watchlist.append(queue[i]['name'])
			queue[i]['guns'] = 0

watchlist = []
watchls(queue)
print(watchlist)

# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

def alcohol_scan (ls1):
	for i in range(0, len(queue)):
		if queue[i]['alcohol'] != 0:
			security_alcohol_loot.append(queue[i]['alcohol'])
			queue[i]['alcohol'] = 0


security_alcohol_loot = []
alcohol_scan(queue)
print(sum(security_alcohol_loot))

print(queue)