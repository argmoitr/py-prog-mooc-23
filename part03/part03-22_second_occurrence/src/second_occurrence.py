# Write your solution here

string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

i1 = string.find(substring)
i2 = string.find(substring, i1+len(substring))
if i2 != -1:
    print(f"The second occurrence of the substring is at index {i2}.")
else:
    print(f"The substring does not occur twice in the string.")
