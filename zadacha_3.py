from random import randint
lst = [randint(-30, 70) for i in range(10)]
'''
Найти сумму всех цифр целочисленного массива. Например, если дан массив [12, 104, 81], то сумма всех его цифр будет 
равна 1 + 2 + 1 + 0 + 4 + 8 + 1 = 17.
'''
print(lst)
count = 0
for i in lst:
	for j in str(i).replace('-',''):
		count += int(j)
print(count)