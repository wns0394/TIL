# num1 = 0.1 * 3
# num2 = 0.3

# import math
# math.isclose(num1,num2)
# print(math.isclose(num1,num2))

# name = '철수'

# print(f'안녕, {name}야')

# # print(str(1))
# print(int('3.5'))

# print(bool('50'))

# n = 5
# m = 9

# print((('*' * n) + '\n') * m)
# print('\"파일은 c:\\wi\\u\\내\\py에 저장이 되었습니다.\"  \n 나는 생각했다. \'cd .\'')


# a = int(input())
# b = int(input())
# c = int(input())

# x1 = (-b + (b ** 2 - 4*a*c)**(1/2)) / (2*a)
# x2 = (-b - (b ** 2 - 4*a*c)**(1/2)) / (2*a)
# print(x1, x2)

# number = int(input())
# for i in range((number+1)):
#     i += 1
#     print(i)

# number = int(input())
# for i in range(number+1):
#     print(number - i)
# number = int(input())
# result = 0
# for i in range(number+1):
#     result += i
#     i += 1
# print(result)

number = int(input())
result = 0
for i in range(1, number+1):
    #result = result + 1
    result += i
    
print(result)