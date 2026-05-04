class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name: " + self.name + ", Cuisine type: " + self.type)

    def open_restaurant(self):
        print("The restaurant is open")


restaurant = Restaurant("Restaurant Name", "Cuisine Type")

print(restaurant.name)
print(restaurant.type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
