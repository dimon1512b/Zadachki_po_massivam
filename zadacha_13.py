from random import randint
lst = [randint(-30, 70) for i in range(10)]

'''
Вывести отдельно первую и отдельно вторую половину массива через срезы.
'''
print(lst[:5], lst[5:])
