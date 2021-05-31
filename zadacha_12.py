from random import randint
lst1 = [randint(-30, 70) for i in range(10)]
lst2 = [randint(-30, 70) for i in range(10)]
'''
Сгенерировать 2 массива. Создать третий массив в котором будут суммы елементов первого массива и второго.
То есть первый елемент будет равен сумме первых елементов первого и второго массива.
'''
lst3 = [0 for i in range(10)]
for i in range(10):
	lst3[i] = lst1[i] + lst2[i]
print(lst3)
