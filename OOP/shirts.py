from shirt import Shirt

new_shirt = Shirt('red', 'S', 'short sleeve', 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(.2))

tshirt_collection = []
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)


tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three )

for i in range(len(tshirt_collection)):
    tshirt_collection[i].color = "black"
    print (tshirt_collection[i].color)