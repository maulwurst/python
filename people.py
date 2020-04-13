people = {
	"Max":{
	'Name': 'Max',
	'Age': '30',
	'Occupation': 'rat',
	},
	
	'Matthias':{
	'Name': 'Matthias',
	 'Age': '22',
	 'Occupation': 'rat',
	 },
}

for name, people in people.items():
	print("\nName:" + name)
	name_and_age = people['Name'] + " "+ people['Age']
	job = people['Occupation']
	
	print("\tName and age: " + name_and_age.title())
	print("\tJob is: " + job.title())
	
