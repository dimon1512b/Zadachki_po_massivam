from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
print(lst.pop(lst.index(min(lst))))
print(lst.pop(lst.index(min(lst))))
