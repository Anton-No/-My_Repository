#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

revenue = int( input( "Введите значеине выручки, "))
costs = int( input( "Введите значеине издержки, "))
if revenue > costs:
    print ("Есть прибыль. Выручка больше издержек. Всё ОК")
elif revenue < costs:
    print ("Убытки. Издержки больше выручки. Работай лучше!")
elif revenue == costs:
    print ("Работа в 0. Работай лучше!")