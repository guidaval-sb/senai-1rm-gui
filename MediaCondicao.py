n1 = float(input("Informe a nota 1: "))
n2 = float(input("Informe a nota 2: "))
n3 = float(input("Informe a nota 3: "))

media = int(n1 + n2 + n3)/3 

if media >= 6:
    print("aprovado")  #identacao é os espaco qe necessario no "if" e "else" aqele tabzinho
elif media >= 5:
        print("vai ja conselho de classe")
else: 
        print("Reprovado")

print("sua media foi: {:.1f}".format(media))