# HomeWork

### Built-in 함수

Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

```
print()
sum()
min()
max()
len()
...
```





### 정중앙 문자 

문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

```python
get_middle_char('ssafy') # => a
get_middle_char('coding') # => di
```

```python
def get_middle_char(word):
    length = 0
    # 단어 전부 순회
    for i in word:
        # 한개씩 개수를 새어보자.
        length += 1
    # 정 중앙값
    center = length // 2

    # 만약 홀수라면
    if length % 2:
        result = word[center]
    # 짝수라면
    else:
        # result = word[center-1] + word[center]
        result = word[center-1:center+1]
    return result
```





### 위치 인자와 키워드 인자

다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는 코드를 고르시오. 

```python
def ssafy(name, location='부울경'):
    print(f'{name}의 지역은 {location}입니다.')
    
# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')

# (4)
ssafy(name='길동', '구미')
```

```
ssafy(name='길동', '구미')
- 키워드 인자를 사용한 뒤에는 위치 인자를 사용 할 수 없다.
```





### 나의 반환값은 

다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a, b):
    c = a + b
    print(c)
    
result = my_func(3, 7)
```

```
None
```



### 가변 인자 리스트

가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정수들의 평균 값을 반환하는 my_avg 함수를 작성하시오.

```python
my_avg(77, 83, 95, 80, 70) # => 81.0
```

```python
def my_avg(*numbers):
    # 평균값을 구하기
    length = 0
    count = 0
    for i in numbers: # (77, 83, ....)
        length += 1
        count += i
    return count / length

print(my_avg(77, 83, 95, 80, 70)) # => 81.0
```

