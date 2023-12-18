# Write your solution here

my_list = []

item = 1
while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove, or e(x)it: ")
    if choice == "x":
        break
    elif choice == "d":
        my_list.append(item)
        item += 1
    elif choice == "r":
        new_item = my_list.pop(len(my_list)-1)
        item = new_item
print("Bye!")
