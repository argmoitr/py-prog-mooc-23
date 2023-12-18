# Write your solution here

def length_of_longest(strings: list) -> int:
    longest_length = len(strings[0])
    for string in strings:
        if longest_length < len(string):
            longest_length = len(string)
    return longest_length

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)
