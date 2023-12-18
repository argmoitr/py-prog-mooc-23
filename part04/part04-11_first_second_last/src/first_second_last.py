# Write your solution here

# Better solution

def find_word(sentence, count):
    i = 0
    word = ""
    spaces = 0
    while i < len(sentence):
        if sentence[i] == " ":
            spaces += 1
            if spaces == count:
                break
            word = ""
        else:
            word += sentence[i]
        i += 1
    return word

def first_word(sentence):
    return find_word(sentence, 1)

def second_word(sentence):
    return find_word(sentence, 2)

def last_word(sentence):
    return find_word(sentence, 0)

# My solution
# 
# def first_word(sentence):
#     i = sentence.find(" ")
#     return sentence[:i]

# def second_word(sentence):
#     i1 = sentence.find(" ")
#     i2 = sentence.find(" ", i1+1)
#     if i2 == -1:
#         return sentence[i1+1:]
#     return sentence[i1+1:i2]

# def last_word(sentence):
#     spaces = sentence.count(" ")
#     i = 0
#     count = 0
#     while i < len(sentence):
#         if sentence[i] == " ":
#             count += 1
#         if count == spaces:
#             break
#         i += 1
#     return sentence[i+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
