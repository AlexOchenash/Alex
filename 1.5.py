revenue = int(input("Выручка: "))
costs = int(input("Издержки: "))
profit = revenue - costs
loss = costs - revenue
if revenue >= costs:
    print("Компания заработала: ", profit)
    profit_margin = profit / revenue * 100
    print("Рентабельности выручки составила: ", profit_margin, "%")
    emp = int(input("Количество сотрудников: "))
    emp_pr = profit / emp
    print("прибыль на одного сутрудника составила: ", emp_pr)
else:
    print("Компания потеряла", loss)



