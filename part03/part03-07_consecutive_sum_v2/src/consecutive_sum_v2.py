# Write your solution here

limit = int(input("Limit: "))

sum = 0
sentence = ""

i = 1
while sum < limit:
    sum += i
    if sum >= limit:
        sentence += f"{i}"
    else:
        sentence += f"{i} + "
    i += 1

print(f"The consecutive sum: {sentence} = {sum}")
