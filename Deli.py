sandwich_orders = ['BLT','Egg','Chicken','pastrami','pastrami','pastrami']
finished_sandwiches = []

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    sandwich_made = sandwich_orders.pop()
    print("I made  your: " + str(finished_sandwiches))
    finished_sandwiches.append(sandwich_made)
    print("your "+ str(finished_sandwiches) +" is finnished")


