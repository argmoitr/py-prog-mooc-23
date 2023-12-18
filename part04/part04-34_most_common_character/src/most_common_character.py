# Write your solution here

# Better solution
def most_common_character(string: str) -> str:
    des_char = string[0]
    for char in string:
        if string.count(des_char) < string.count(char):
            des_char = char
    return des_char

# My solution
#
# def most_common_character(string: str) -> str:
#     counts = []
#     for char in string:
#         counts.append(string.count(char))
#     for char in string:
#         if string.count(char) == max(counts):
#             return char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
