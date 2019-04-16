'''
Tarea para Ana. Explorar la documentacion de python,
los built-in types, funciones y librerias
'''
import math
import random
import statistics as stats



#Ejemplos para built in types
set1 = {'este', 'es', 'un', 'set'}

set2 = {'este', 'es', 'otro', 'set', 'diferente'}

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.symmetric_difference(set2))

# print(set1.discard('no'))
#
# print(set2.pop())
#
# print(set2)


#Ejemplos para built in functions
#reversed
arr = [1, 2, 3, 4, 5, 6]

for item in reversed(arr):
    print(item)

for item in reversed('Will it work?'.split()):
    print(item)

sentence_rev = [x for x in reversed('Will it work?'.split())]
print(' '.join(sentence_rev))

#bool
print()
name = None
name2 = 'Sara'
name3 = 1
name4 = 0
name5 = []
name6 = ''

# print(bool(name))
# print(bool(name2))
# print(bool(name3))
# print(bool(name4))
# print(bool(name5))
# print(bool(name6))

#divmod
print()
# print(divmod(16, 3))
# print(divmod(1532, 6))

#filter
print()
for item in filter(lambda x: x % 2 == 0, arr):
    print(item)


for item in filter(lambda x: x > 3, arr):
    print(item)


#help
print()
arr.reverse()
print(arr)

print('trying.new.things'.replace('.', ' '))
print('44353'.isdigit())
print('4324'.isnumeric())
#help(arr)
#help(str)

#Ejemplos para librerias
print()
random_list = [x * random.randint(0,10) for x in range(100)]

print(stats.mean(random_list))
print(stats.median(random_list))
print(stats.median_low(random_list))
print(stats.median_high(random_list))
print(stats.pstdev(random_list))
print(stats.pvariance(random_list))
print()
print(random_list)
