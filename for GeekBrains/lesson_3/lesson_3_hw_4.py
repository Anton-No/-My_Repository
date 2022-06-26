#4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.

#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.



def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Введите действительное число')
        return
    if x <= 0 or y >= 0:
        print("Введите положительный х и отрицательный у")
        return
    return x ** y 


print(round(my_func(2, -2), 10))