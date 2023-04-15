"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X
"""
import random
from random import randint
numb_len = int(input("Enter the amount of elements:"))
numb_list = [randint(0, 10) for _ in range(numb_len)]
search_numb = (randint(0, 10))
step = 0
mini = 10
nearby = []
print(numb_list)
print(search_numb)
for i in range(numb_len):
    nearby.append(abs(numb_list[i] - search_numb))
    if (nearby[i] < mini and nearby[i] > 0):
        mini = nearby[i]
        step = i

print("The desired number", search_numb, "is the list", (numb_list.count(search_numb)), "times")
print("Сlosest element to the desired element is", numb_list[step])
