# def get_secret_word(numbers):
#     # 최종 반환 할 값
#     result = ''
#     # 전체 리스트 순회
#     for num in numbers:
#         # 각 요소들 -> 정수를 문자열로 변환
#         # 변환한 문자열을 result에 더해 나간다.
#         result += chr(num)
#     return result

# print(get_secret_word([83, 115, 65, 102, 89])) # => 'SsAfy'


def get_secret_number(word):
    result = 0
    for char in word:
        result += ord(char) # 't' -> 116
    return result

print(get_secret_number('tom')) # => 336


def get_strong_word(word1, word2):
    # 각 문자열들 아스키 숫자로 변환해서 더할 값
    word1_result = 0
    word2_result = 0

    for char in word1:
        word1_result += ord(char)

    for char in word2:
        word2_result += ord(char)

    # 만약에 word1에 대한 결과가 word2에 대한 결과보다 크다면
    if word1_result > word2_result:
        # 처음 입력 받은 word1을 반환
        return word1
    else:
        return word2


get_strong_word('z', 'a') # => 'z'
get_strong_word('tom', 'john') # => 'john'