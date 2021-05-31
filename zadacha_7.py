from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
Найти среднее арифметическое положительных элементов.
'''
lst = [i for i in lst if i >= 0]
print(sum(lst)/len(lst))
