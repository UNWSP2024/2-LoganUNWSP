# item is in float/decimal, then the type is printed to verify it is a float
item1 = float(input("Enter cost of your first Item: "))
print(type(item1))
item2 = float(input("Enter cost of your second Item: "))
print(type(item2))
item3 = float(input("Enter cost of your third Item: "))
print(type(item3))
item4 = float(input("Enter cost of your fourth Item: "))
print(type(item4))
item5 = float(input("Enter cost of your fifth Item: "))
print(type(item5))

#add the subtotal then print it, using f to format
subtotal = item1 + item2 + item3 + item4 + item5
print(f"Your subtotal is {subtotal: .2f}")

#add the tax amount by getting tax rate times sub total, using f to format
tax_amount = subtotal * .07
print(f"Tax will be {tax_amount: .2f}")

#adding subtotal and tax to get the total, using f to format
total = subtotal + tax_amount
print(f"This will cost you {total: .2f}")
