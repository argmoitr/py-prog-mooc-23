# Write your solution here

word = input("Word: ")

print("*" * 30)
spaces = (30 - len(word) - 2) // 2
if len(word) % 2 == 0:
    print("*" + " " * spaces + word + " " * spaces + "*")
else:
    print("*" + " " * spaces + word + " " * (spaces + 1) + "*")
print("*" * 30)
