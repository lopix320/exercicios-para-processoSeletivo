string = 'arroz'
stringReverse = ''
for x in range(1, string.__len__() + 1):
    stringReverse += string[-x]

print(stringReverse)
