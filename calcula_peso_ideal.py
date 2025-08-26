altura = float(input("Digite a altura:"))

genero = input("Digite o genero(M/F):")

if genero == "F":
   peso = ((62.1*altura)-44.7)
else:
   peso = ((72.7*altura)-58)

print(f"{peso:.2f}")