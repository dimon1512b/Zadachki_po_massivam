from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
Вывести каждое третье число в массиве через интервалы среза.
'''
print(lst[2::3])
