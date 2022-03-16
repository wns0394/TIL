# def get_secret_word(numbers):
#     result = ''
#     for number in numbers:
#         result += chr(number)
#     return result

# print(get_secret_word([83, 115, 65, 102, 89]))



# def get_secret_number(word):
#     result = 0
#     for i in word:
#         result += ord(i)
#     return result
# print(get_secret_number('tom'))

def get_strong_word(word1, word2):
    result1 = 0
    result2 = 0
    for i in word1:
        result1 += ord(i)
    for j in word2:
        result2 += ord(j)
    if result1 > result2:
        return word1
    else:
        return word2
print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))
    
