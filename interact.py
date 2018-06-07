import core

bruto_income = float(input("enter (bruto) salary "))
net_income = core.net_income(bruto_income)
savings = core.savings(bruto_income)
print("net income is: " + str(int(net_income)) + "\nsavings are " + str(int(savings)))
