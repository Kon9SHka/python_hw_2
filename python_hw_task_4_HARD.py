#задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе
# 

k = int(input("Введите число: "))

def Fill_array (k):
    a = list()
    for i in range(k*2+1):
            a.insert(i,"_")
    return a

def fibonaccy_function (k, array):
    for i in range(k+1):

        if i == 0:
            array[k]=0

        elif i==1:
            array[k+i]=1
            array[k-i]=1
        else:
            array[k+i]=array[k+i-2]+array[k+i-1]
            array[k-i]=(-1)**(i+1)*array[k+i]

    return array

fib_numbers = Fill_array(k)
fib_numbers = fibonaccy_function(k, fib_numbers)

print(fib_numbers)