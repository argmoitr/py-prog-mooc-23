# Write your solution here

def all_the_longest(strings: list) -> list:
    des_list = []
    longest_length = len(strings[0])
    for string in strings:
        if longest_length < len(string):
            longest_length = len(string)
    for string in strings:
        if len(string) == longest_length:
            des_list.append(string)
    return des_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
