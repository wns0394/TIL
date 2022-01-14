# import 시 주의할 점
# import 가지고 오는 행위
# 이 이후로 활용할 코드를 가지고 올 것이기 때문에
# import는 항상 최 상단에 작성한다.
# import는 켜자마자 하지말고 필요할때 작성하자 !!

import random

menu = ['짜장면', '짬뽕', '탕수육']
# menu 중에 하나를 무작위로 선택
choice = random.choice(menu)

print(choice)