# 1. len(), print(), max(), min(), abs()



# def get_middle_char(word):
#     length = 0
#     result = ''
#     for i in word:
#         length += 1
#         if length % 2:
#             result = word[length//2]
#         else:
#             result = word[length//2 - 1:length//2 + 1] 
#     return result

# print(get_middle_char('ask'))
# print(get_middle_char('coding'))

# 3. 정답은 (4)번 이유는 name에 길동이 들어가고 '구미가 지정되어있지 않다.

# 4. none값이 저장되어있다. my_func을 선언하고 c에대한 반환을 해주지 않았기 때문에

# # 5. 
# def my_avg(args):
#     total = 0
#     length = 0
#     for i in args:
#         length += 1
#         total += i
#     return total / length

# print(my_avg(77, 83, 95, 80, 70))

#workshop 
# # 1.
# def list_sum(numbers):
#     result = 0
#     for i in numbers:
#         result += i
#     return result


# print(list_sum([1, 2, 3, 4, 5])) # => 15

# def dict_list_sum(infos):
#     result = 0
#     for i in infos:
#         result += i['age']
#     return result
# print(dict_list_sum([{'name': 'kim', 'age': 12},{'name': 'lee', 'age': 4}])) # => 16

# 3.
# def all_list_sum(numbers):
#     result = 0
#     for number in numbers:
#         for i in number:
#             result += i
#     return result
# print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))