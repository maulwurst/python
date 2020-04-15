sandwich_orders = ['BLT','Egg','Chicken','pastrami','pastrami','pastrami']
finished_sandwiches = []

while sandwich_orders:
	sandwich_made = sandwich_orders.pop()
	print("I made  your: " + str(finished_sandwiches))
	finished_sandwiches.append(sandwich_made)

for sandwich_order in finished_sandwiches:
	print(finished_sandwiches)
