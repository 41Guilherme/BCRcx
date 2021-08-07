string = input("")
lista = []
for i in string:
    if i not in lista:
        lista.append(i)

x = len(string) - len(lista)

print(x)