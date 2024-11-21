from itertools import permutations

str1 = 'base'
str2 = 'ball'
result = 'games'

a = sorted(set(str1) | set (str2) | set(result))

for values in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(a)):
    d = dict(zip(a, values))
    num1 = ''.join(str(d[i]) for i in str1)
    num2 = ''.join(str(d[i]) for i in str2)
    tot = ''.join(str(d[i]) for i in result)
    if int(num1) + int(num2) == int(tot):
        print(d)
        break