# WorkShop

### List의 합 구하기

정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
list_sum([1, 2, 3, 4, 5]) # => 15
```

```
def list_sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(list_sum([1, 2, 3, 4, 5])) # => 15
```



### Dictionary로 이루어진 List의 합 구하기

Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value 들의 합을 반환하는 dict_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오. 

```python
dict_list_sum([{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}]) # => 16
```

```python
def dict_list_sum(infos):
    # 모든 age들을 더할 변수
    result = 0
    # 순회
    for info in infos:
        result += info['age'] # dict -> {'name': 'kim', 'age': 12}
    return result

print(dict_list_sum([{'name': 'kim', 'age': 12},{'name': 'lee', 'age': 4}])) # => 16
```





### 2차원 List의 전체 합 구하기

정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```python
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) # => 55
```

```python
def all_list_sum(numbers):
    result = 0
    for number in numbers: # number -> [1], [2, 3] ...
        for num in number: # num -> 1, 2, 3, ...
            result += num
    return result

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])) # => 55
```

