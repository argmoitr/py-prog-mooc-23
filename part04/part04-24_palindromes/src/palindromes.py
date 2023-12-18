# Write your solution here

def palindromes(text: str) -> bool:
    if len(text) <= 1:
        return True
    for i in range(len(text)):
        if text[i] != text[len(text)-1-i]:
            return False
    return True

def main():
    while True:
        string = input("Please type in a palindrome: ")
        if palindromes(string):
            break
        print("that wasn't a palindrome")
    print(f"{string} is a palindrome!")

main()

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
