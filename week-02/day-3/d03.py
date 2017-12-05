# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

def ret (accs):
    for i in accounts:
        print(i['client_name'], i['balance'])

ret(accounts)


def transfer(ls):
	a = int(input('From: '))
	b = int(input('To: '))
	c = int(input('Amounts: '))
	error = []
	error1 = []
	for i in accounts:
		if a != i['account_number']:
			error.append(1)
			pass
		else:
			for j in accounts:
				if j['account_number'] != b:
					error1.append(1)
					pass
				else:
					i["balance"] -= c
					j['balance'] += c
					print(accounts)
	if len(error) == len(accounts) or len(error1) == len(accounts):
		print("404 - account not found")	
		
transfer(accounts)