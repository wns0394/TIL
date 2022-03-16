# WorkShop

### 간단한 N의 약수 (SWEA #1933)

입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램 을 작성하시오.

```
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

[입력]
입력으로 정수 N이 주어진다.

[출력]
정수 N의 모든 약수를 오름차순으로 출력한다.

[입력 예시]
10

[출력 예시]
1 2 5 10
```

```python
N = int(input())

for i in range(1, N+1):
    # N 나누기 i의 나머지가 0이라면
    if N % i == 0:
        print(i, end=' ')
```





### 중간값 찾기 (SWEA #2063 변형) 

중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

```python
[출력 예시]
64
```

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]
```

```python
sorted_numbers = sorted(numbers)

length = 0
for i in numbers:
    length += 1

center = length // 2
# center = len(sorted_numbers) // 2
print(sorted_numbers[center])
```



### 계단 만들기 

자연수 number를 입력 받아, 아래와 같이 높이가 number인 내려가는 계단을 출력하시오

```
[입력 예시]
4

[출력 예시]
1
1 2
1 2 3
1 2 3 4 
```

```python
N = int(input())
N = 4

for i in range(1, N+1):
	for j in range(1, i+1):
        print(j, end=' ')
    print()
```

