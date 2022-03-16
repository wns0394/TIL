# WorkShop

### 숫자의 의미

정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하 그리고 97이상 122이하의 정수로만 구성되어 있다.

```python
get_secret_word([83, 115, 65, 102, 89]) # => 'SsAfy'
```

```python
def get_secret_word(numbers):
    # 최종 반환 할 값
    result = ''
    # 전체 리스트 순회
    for num in numbers:
        # 각 요소들 -> 정수를 문자열로 변환
        # 변환한 문자열을 result에 더해 나간다.
        result += chr(num)
    return result

print(get_secret_word([83, 115, 65, 102, 89])) # => 'SsAfy'
```





### 내 이름은 몇일까? 

문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는 get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.

```python
get_secret_number('tom') # => 336
```

```python
def get_secret_number(word):
    result = 0
    for char in word:
        result += ord(char) # 't' -> 116
    return result

print(get_secret_number('tom')) # => 336
```



### 강한 이름

문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.

```python
get_strong_word('z', 'a') # => 'z'
get_strong_word('tom', 'john') => 'john'
```

