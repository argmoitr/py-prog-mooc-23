# Write your solution here

year = int(input("Year: "))

start_year = year + 1
leap_year = False

while True:
    if start_year % 100 == 0:
        if start_year % 400 == 0:
            leap_year = True
    elif start_year % 4 == 0:
        leap_year = True
    if not leap_year:
        start_year += 1
    else:
        break

print(f"The next leap year after {year} is {start_year}")
