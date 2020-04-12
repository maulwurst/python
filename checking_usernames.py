current_users = ['Max','Matthias','person3','Marga','Albin']
new_users = ['Person1','Person2','Person3','Person4','Person5']

for new_user in new_users:
	if new_user in current_users:
		print('That username is taken')
	else:
		print('That username is available.')
