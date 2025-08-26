genero = input("Digite o genero(M/F):")

h = int(input("Digite a altura:

if genero == "F":
   peso = ((62.1*h)-44.7)
else:
   peso = ((72.7*h)-58)

print(f"Seu peso ideal é {peso:.2f}")
