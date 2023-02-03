"""Задача 5 - HARD необязательная
Напишите программу, которая принимает на вход координаты двух точек и находит 
расстояние между ними в N-мерном пространстве. Сначала задается N с клавиатуры, потом задаются координаты точек."""

def Coord_fill (N,x):
    a = list()
    for i in range(N):
        a.insert(i,int(input(f'Введите {i+1} координату точки {x}: ')))
    return a

def Sum_square (coord_x, coord_y,N):
    sum=0
    for i in range(N):
        sum = sum + (coord_y[i]-coord_x[i])**2
    return sum**0.5
    

N = int(input("Введите число N: "))

coord_x = Coord_fill(N,"x")
print(coord_x)
coord_y = Coord_fill(N,"y")
print(coord_y)

print(Sum_square(coord_x,coord_y,N))