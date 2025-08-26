altura = float(input("Digite a altura:"))

genero = input("Digite o genero(M/F):")

if genero == "F":
   peso = ((62.1*h)-44.7)
else:
   peso = ((72.7*h)-58)

print(f"{peso:.2f}")