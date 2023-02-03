#задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

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