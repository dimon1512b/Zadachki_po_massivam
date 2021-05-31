from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
Найти в массиве те элементы, значение которых меньше среднего арифметического, взятого от всех элементов массива.
'''
a = sum(lst) / len(lst)

print([elem for elem in lst if elem < a])
