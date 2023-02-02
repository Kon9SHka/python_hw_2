#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))
i = 0
all_numbers = list()
while 2 ** i <= N:
    all_numbers.insert(i,2 ** i)
    i+=1
print(all_numbers)