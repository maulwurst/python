class Restaurant:
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        
    def describe_restaurant(self):
        print(self.name.title() + ' ' + self.cuisine)
    
    def open_restaurant(self):
        print("is open")

restaurant = Restaurant('india gate','indian')

print(restaurant.name.title() + " "+ restaurant.cuisine.title())

restaurant.open_restaurant()
restaurant.describe_restaurant()


