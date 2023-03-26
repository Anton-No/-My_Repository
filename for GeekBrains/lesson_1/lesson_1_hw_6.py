#6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.



revenue = int( input( "Введите значеине выручки, "))
costs = int( input( "Введите значеине издержки, "))
if revenue > costs:
    print ("Есть прибыль. Выручка больше издержек. Всё ОК")
    return_on_revenue = (revenue - costs) / revenue
    print ( "Рентабельность выручки: ", return_on_revenue)
    employee = int( input( "Введите количество сотрудников компании, "))
    profit_per_employee = (revenue - costs) / employee
    print ( "Прибыль на одного сотрудника: ", profit_per_employee )
elif revenue < costs:
    print ("Убытки. Издержки больше выручки. Работай лучше!")
elif revenue == costs:
    print ("Работа в 0. Работай лучше!")