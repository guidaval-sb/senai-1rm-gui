salario = float(input("Qual é o seu salario? "))
if salario > 8250.00:
    reajuste = salario * 1.10
else: 
    reajuste = salario * 1.15
print("seu novo salario é {:.2f} ".format(reajuste))