# def my_abs(x):
#     if type(x) == complex:
#         return (x.real**2 + x.imag**2)**(1/2)
#     else:
#         if x == 0:
#             return x**2
#         elif x >= 0:
#             return x
#         else:
#             return x * -1
# print(my_abs(0.0))
# print(my_abs(3+4j))
# print(my_abs(-0.0))
# print(my_abs(-5))
# print(abs(3+4j), abs(-0.0), abs(-5)) 

# def my_all(elements):
#     for element in elements:
#         if not element:
#             return False
#     return True
# print(my_all([]))
# print(my_all([1, 2, 5, '6']))
# print(my_all([[], 2, 5, '6']))
# print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

# def my_any(elements):
#     for element in elements:
#         if not element == False:
#             return True
#     return False
# print(my_any([]))
# print(my_any([1, 2, 5, '6']))
# print(my_any([[], 2, 5, '6']))
# print(my_any([0]))
# print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))

# practice 2

#1.1 불쌍한 달팽이

# def snail(height, day, night):
#     count = 0
#     dis = 0
#     while dis <= height:
#         count += 1
#         dis += day
#         if dis >= height:
#             return count
#         dis -= night
# print(snail(100,5,2))

# 1.2 자리수 더하기
# def sum_of_digit(number):
#     result = 0
#     while number % 10 >= 0:
#         result += number % 10
#         number = number // 10
#     return result
# print(sum_of_digit(12340))

# print(0  % 10)

# def sum_of_recursive(number):
#     result = 0
#     if number / 10 > 0:
#         result += number % 10
#         number = number // 10
#         return result + sum_of_recursive(number)
# print(sum_of_recursive(1234))

######## 재귀함수 종료 조건
# def sum_of_recursive(number):
#     result = 0
#     # 종료 조건
#     if number == 0:
#         return number
#     else:
#         result += number % 10
#         number = number // 10
#         return sum_of_recursive(number) + result
# print(sum_of_recursive(1234))

# print(1//10)

### pracitce 3

# ### 1.1 회문판별

# def is_pal_while(word):
#     a = len(word)
#     for i in range(1,a+1):
#         if word[i] == word[-1-i]:
#             return True
#         else:
#             return False
# print(is_pal_while('tomato')) #=> False
# print(is_pal_while('racecar')) #=> True

# def is_pal_while(word):
#     result = 0
#     while result <= len(word) //2:
#         if word[result] == word[-1-result]:
#             result += 1
#             return True
#         else:
#             return False
# print(is_pal_while('tomato')) #=> False
# print(is_pal_while('racecar')) #=> True

# def is_pal_while(word):
#     while len(word) > 1:
#         if word[0] == word[-1]:
#             word = word[1:-1]
#             return True
#         else:
#             return False
# print(is_pal_while('tomato')) #=> False
# print(is_pal_while('racecar')) #=> True

######### 재귀함수는 종료조건을 생각하자

# def is_pal_while(word):
#     if len(word) <= 1:
#         return True
#     else:
#         if word[0] == word[-1]:
#             word = word[1:-1]
#             return is_pal_while(word)
#         else:
#             return False
    
# print(is_pal_while('tomato')) #=> False
# print(is_pal_while('racecar')) #=> True