# Write your solution here

value_of_gift = int(input("Value of gift: "))

if value_of_gift < 5000:
    amount = 0
elif value_of_gift < 25000:
    tax = 100
    tax_rate = 0.08
    amount = (tax + (value_of_gift - 5000) * tax_rate)
elif value_of_gift < 55000:
    tax = 1700
    tax_rate = 0.10
    amount = (tax + (value_of_gift - 25000) * tax_rate)
elif value_of_gift < 200000:
    tax = 4700
    tax_rate = 0.12
    amount = (tax + (value_of_gift - 55000) * tax_rate)
elif value_of_gift < 1000000:
    tax = 22100
    tax_rate = 0.15
    amount = (tax + (value_of_gift - 200000) * tax_rate)
else:
    tax = 142100
    tax_rate = 0.17
    amount = (tax + (value_of_gift - 1000000) * tax_rate)

if amount == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {amount} euros")
