#7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).

#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.

#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#Подсказка: использовать менеджер контекста.



import json

res = dict()
ave_profit = 0
num = 0
with open('/Users/an/Documents/My_Repository/for GeekBrains/lesson_5/text_7.txt', encoding='utf-8') as f:
    for line in f:
        name, type, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit >= 0:
            ave_profit += profit
            num +=1
        res[name] = profit
ave_profit /= num
with open("jsone7.json", "w", encoding="utf-8") as f:
    json.dump([res, {"ave_profit": ave_profit}], f, ensure_ascii=False)