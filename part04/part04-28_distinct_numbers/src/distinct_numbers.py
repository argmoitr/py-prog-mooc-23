# Write your solution here

def distinct_numbers(numbers: list) -> list:
    new_list = []
    for num in sorted(numbers):
        if num in new_list:
            continue
        new_list.append(num)
    return new_list

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]
