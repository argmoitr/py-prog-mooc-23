# Write your solution here

def shortest(strings: list) -> str:
    string_shortest = strings[0]
    for string in strings:
        if len(string_shortest) > len(string):
            string_shortest = string
    return string_shortest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
