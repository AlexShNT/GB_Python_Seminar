'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
с повторениями). Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами
элементы множеств.
'''

# n = int(input('n: '))
# m = int(input('m: '))

# a1 = a2 = []

# for i in range(n):
#     a1.append(int(input(f'n {i}: ')))

# for i in range(m):
#     a1.append(int(input(f'm {i}: ')))

# a = sorted([x for x in set(a1 + a2)])

# print(a)

'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растёт на круглой грядке, причём кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке
растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

3 1 2 4
'''

# a = [1,3,9,7,4,10,2]

n = int(input('n: '))

a =  []

for i in range(n):
    a.append(int(input(f'n {i}: ')))


print(max(sum([a[i-2], a[i-1], a[i]]) for i in range(len(a))))



