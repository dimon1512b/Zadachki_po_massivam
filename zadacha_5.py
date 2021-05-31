from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
Найти и вывести на экран наибольший его элемент и порядковый номер этого элемента.
'''

print(max(lst), lst.index(max(lst))+1)
