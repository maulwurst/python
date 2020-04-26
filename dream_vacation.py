places_to_visit = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhere would you like to visit ")
    
    places_to_visit[name] = response
    
    repeat = input("type no to quit or add more destinations ")
    if repeat == 'no':
        polling_active = False
    
for name, response in responses.items():
    print(name + "would like to visit" + response)
    
