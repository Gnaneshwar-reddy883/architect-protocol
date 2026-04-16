menu = {"pizza":6,
        "nachos":3,
        "coke":1.5,
        "chips":2,
        "bread":2,
        "C65" : 3}
cart = []
total = 0
print("-------menu-------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

while True:
    food = input("enter the food item(q to quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------your order-----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"your total is ${total:.2f}")