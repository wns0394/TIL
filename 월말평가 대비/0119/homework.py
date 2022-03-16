# 정중앙 문자를 반환 하는 함수
# 만약 문자열의 길이가 짝수라면 중앙의 2개를 반환
# 함수를 정의
# 전달인자를 받을 매개변수
# ctrl + / => 내가 선택한 줄 모두 주석처리    
def get_middle_char(word):
    length = 0
    # 단어 전부 순회
    for i in word:
        # 한개씩 개수를 새어보자.
        length += 1
    # 정 중앙값
    center = length // 2

    # 만약 홀수라면
    if length % 2: # length % 2 == 1
        result = word[center]
    # 짝수라면
    else:
        # result = word[center-1] + word[center]
        result = word[center-1:center+1]
    return result


print(get_middle_char('ssafy')) # => a
print(get_middle_char('coding')) # => di

# def my_func(a, b):
#     c = a + b
#     print(c)
#     return c
    
# result = my_func(3, 7)
# print(result)


# 함수 정의
# 가변 인자 리스트 -> 다수의 인자들을 한번에 받아 보자.
# def my_avg(*numbers):
#     # 평균값을 구하기
#     length = 0
#     count = 0
#     for i in numbers: # (77, 83, ....)
#         length += 1
#         count += i
#     return count / length

# print(my_avg(77, 83, 95, 80, 70)) # => 81.0

# def test(list_a, list_b):
#     print(list_a, list_b)

# test(*[['첫번째 인자'],  ['두번째 인자']])

# print(*[['첫번째 인자'],  ['두번째 인자']])

# 그리고 사실 다른것보다 이게 제일 꿀팁이 될거 같아요
# 그게 뭐냐면
# 코드 순서 바꾸기 alt + 위/아래
