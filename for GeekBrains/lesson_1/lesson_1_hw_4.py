#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.



number = int( input( "Введите целое положительное число, "))
maximum = 0
while number > 0:
     last = number %10
     if last > maximum:
          maximum = last
     number = number //10
print( "Максимальное число:", maximum)