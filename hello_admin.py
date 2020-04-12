usernames = ['admin','max']
if usernames:
	for username in usernames:
		if username == 'admin':
			print('Welcome admin')
		else:
			print('Welcome ' + username ' Thanks for logging in')
			
else:
	print("We need more users")
