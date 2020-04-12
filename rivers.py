rivers = {'nile': 'egypt',
          'amazon': 'brazil',
		  'danube': 'austria',
		  'rhine': 'germany',
		  'colorado': 'usa'
		  }
for river in set(rivers.values()):
	print("The " + river.title())
