# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = int(input ('Введите время в секундах: '))
hour = int(time_in_sec /3600)
minutes = (time_in_sec - hour * 3600) // 60
seconds = time_in_sec %60
print ("%.2d" % hour,":", "%.2d" % minutes,":", "%.2d" % seconds)