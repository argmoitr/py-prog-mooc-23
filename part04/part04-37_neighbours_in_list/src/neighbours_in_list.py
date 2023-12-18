# Write your solution here

# Better solution

def longest_series_of_neighbours(numbers: list) -> int:
    neighbours = 1
    max_neighbours = 1
    for i in range(len(numbers)-1):
        if abs(numbers[i+1]-numbers[i]) == 1:
            neighbours += 1
        else:
            neighbours = 1
        max_neighbours = max(neighbours, max_neighbours)
    return max_neighbours

# My solution
#
# def longest_series_of_neighbours(numbers: list) -> int:
#     neighbours = 0
#     max_neighbours = 0
#     neighbour_found = False
#     for i in range(len(numbers)-1):
#         if abs(numbers[i+1]-numbers[i]) == 1:
#             neighbour_found = True
#             neighbours += 1
#             if neighbours > max_neighbours:
#                 max_neighbours = neighbours
#         else:
#             neighbours = 0
#     return max_neighbours + 1

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
