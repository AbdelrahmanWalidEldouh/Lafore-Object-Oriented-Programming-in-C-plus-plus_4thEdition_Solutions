sandwich_orders = ["tuna", "chicken", "beef", "cheese", "veggie"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
