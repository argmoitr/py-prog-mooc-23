# Write your solution here

def mean(integers: list) -> float:
    return sum(integers) / len(integers)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)
