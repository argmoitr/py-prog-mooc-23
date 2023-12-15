# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

i = word.find(char)
while i != -1 and i + 3 <= len(word):
    if len(word) == 0:
        break
    i = word.find(char)
    print(word[i:i+3])
    word = word[word.find(char, i+1):]
