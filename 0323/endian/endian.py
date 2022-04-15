import sys

print(sys.byteorder)
print()

a = 1234
# 정수 12를 8비트 리틀 엔디안으로 표기하기
n = int.to_bytes(a, byteorder='little', length=4)
print(n)

# 정수 12를 8비트 빅 엔디안으로 표기하기
n = int.to_bytes(a, byteorder='big', length=4)
print(n)
print()

print(int.from_bytes(n, byteorder='big'))
print(int.from_bytes(n, byteorder='little'))