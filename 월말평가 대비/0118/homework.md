# HomeWork

### Mutable & Immutable

주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

```python
String, List, Tuple, Range, Set, Dictionary
```

 ```
 immutable : string, tuple, range
 mutable : list, set, dictionary
 ```





### 홀수만 담기

range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.

```python
a = list(range(1, 51))
# b = a[0:-1:2]
b = a[::2]
```





### Dictionary 만들기

반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

```python
student = {'김구현': 19, 'viktor': 20}
```





### 반복문으로 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

```python
n = 5
m = 9
```

```python
for height in range(m):
    print('*' * n)
    
for height in range(m):
    for width in range(n):
        # 프린트 함수가 가진 줄바꿈을 실행되지 않도록 설정
        print('*', end='')
    print()
```





### 조건 표현식 

주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오. 

```python
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
```

```python
# 참일때 출력 {조건문} 거짓일때 출력
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```





### 평균 구하기

주어진 list에 담긴 숫자들의 평균값을 출력하시오.

```python
scores = [80, 89, 99, 83]
```

```python
# 전체 값을 다 더해줄 변수
total = 0
# list scores의 길이
# len(scores)
# 전체 길이를 구할 변수
length = 0
for score in scores:
    total += score
    length += 1

print(total / length)
```

```python
print(sum(scores) / len(scores))
```

