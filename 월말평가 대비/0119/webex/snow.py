import random
from time import sleep

while True:
    snow = '*'
    for i in range(90):
        if random.randint(0, 1):
            snow += '*'
        else:
            snow += ' '
    print(snow)
    sleep(0.5)