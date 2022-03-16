### 세로로 출력하기 

자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한줄씩 출력하시오.

```
[입력 예시]
10

[출력 예시]
1
2
3
4
5
6
7
8
9
10
```

```python
# 형 변환을 통해 정수 10을 변수에 담는다.
number = int(input())
# range 함수에 사용 할 수 있다.
for i in range(1, number+1):
    print(i)
```



### 거꾸로 세로로 출력하기

자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한줄씩 출력하시오.

```
[입력 예시]
5

[출력 예시]
5
4
3
2
1
0
```

```python
number = int(input())

for i in range(number, -1, -1):
    print(i)
```





### N줄 덧셈 (SWEA #2025) 

입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한 값 을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가 10일 경우 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55이므로, 출력해야 할 값은 55이다.

```
[입력 예시]
10

[출력 예시]
55
```

```python
# 값 입력 받기
number = int(input())

# 출력 할 최종 값
result = 0
for i in range(1, number+1):
    # result = result + i
    result += i

print(result)

print(sum(range(1, number+1)))
```

