foods = []
prices = []
total = 0
while True:
    food = input("enter a food to buy(q to quit): ")
    if food.lower()== "q":
        break
    else:
        price = float(input(f"enter the price of the {food} :$"))
        foods.append(food)
        prices.append(price)

print("------YOUR CART------")
for i in range(len(foods)):
    food = foods[i]
    price = prices[i]
    print(f"{food} = ${price}")
    total = total + price
print()
print(f"your cart total price is {total}")


