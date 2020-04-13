pets = {'Mittens':{
		'type': 'cat',
		'owners name': 'Mum',
			},
		'Leary':{
		'type': 'cat',
		'owners name': 'Max',
		},
		'Jesse':{
		'type': 'dog',
		'owners name': 'Rosie',}
		}
		
for name, pets in pets.items():
	print('\n Pets name is: ' +name)
	animal = pets['type']
	master = pets['owners name']
	print('and that pet is a '+ animal + ' and their owner is ' + master)
