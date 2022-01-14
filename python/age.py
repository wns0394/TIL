# requests 불러오기
# 나이 예측 api 사용
# 틀정 이름을 입력 했을 때, 무작위 나이를 가져와서
# ~~의 나이는 ~~살 입니다. 라는 문자를 출력
import requests

name = input('이름을 입력해 주세요 : ')
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()

age = response['age']

print(f'{name}의 나이는 {age}살 입니다.')