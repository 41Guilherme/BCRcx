
n = int(input(""))
s = input("")
lista = [s]
lista2= []
for i in range(n):
    linha = input("")
    lista2.append(linha)

for i in lista2:
    if i in lista:
        print(i)