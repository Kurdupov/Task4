import random
t = int(random.uniform(1,11))
a = int(input('Яке число ?'))
while True:
    s = int(input(a))
    if s < t:
        print('більше')
    elif s>t:
        print('менше')
    else: # s==t
     print('молодець')
    break