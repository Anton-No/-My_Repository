#3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

#Пример файла:

#Иванов 23543.12
#Петров 13749.32



with open('/Users/an/Documents/My_Repository/for GeekBrains/lesson_5/text_3.txt', 'r', encoding='utf-8') as f:
    names = []
    av_income = 0
    num = 0
    for line in f:
        num += 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < 20000:
            names.append(name)
        av_income += income
    av_income /= num
print(*names)
print(av_income)