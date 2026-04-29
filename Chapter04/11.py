pizzas = ["Margherita", "Pepperoni", "Hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append("BBQ Chicken Pizz")
friend_pizzas.append("Vegetarian Pizza")

print("My favorit pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorit pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
