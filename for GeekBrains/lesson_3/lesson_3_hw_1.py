#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

from msilib.schema import Error


def div(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print("Деление на 0")
    except ValueError:
        print('Введите цифры')
        
        
print(div(input(), input()))