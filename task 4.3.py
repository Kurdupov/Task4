from itertools import combinations
a=input('Введіть речення:')
output = sum([list(map(list, combinations(a, i))) for i in range(len(a) + 1)], [])
print(output)