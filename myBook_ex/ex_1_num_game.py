import random

a = random.randint(0, 100)
left = 0
right = 100
while True:
    print('当前范围是：', left, '---', right)
    test = int(input('猜一下\n'))
    if test == a:
        print('^_^')
        break
    if test > a:
        right = test
    else:
        left = test
