from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
В массиве найти максимальный элемент с четным индексом.
'''
print(max(lst[::2]))