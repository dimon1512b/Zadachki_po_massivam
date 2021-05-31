from random import randint
lst1 = [randint(-30, 70) for i in range(10)]
lst2 = [randint(-30, 70) for i in range(10)]
'''
Сгенерировать 2 массива рандомными числами. После посчитать общую сумму их елементов.
'''
print(sum(lst1)+sum(lst2))
