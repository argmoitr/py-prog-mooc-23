# Write your solution here

def range_of_list(integers: list) -> int:
    return max(integers) - min(integers)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print("The range of the list is", result)
