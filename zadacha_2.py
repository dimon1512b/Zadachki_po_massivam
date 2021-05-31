from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
В массиве, содержащем положительные и отрицательные целые числа, вычислить сумму четных положительных элементов
'''
count = 0
for i in lst:
	if (i % 2 == 0) and i >= 0:
		count += i
print(count)
