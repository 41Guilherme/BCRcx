def arrasta(lista):
    x1 = lista[0]
    lista.pop(0)
    lista.append(x1)
    return lista


n1 = int(input(""))
n2 = int(input(""))
lista = []

for i in range(n1):
    y = int(input(""))
    lista.append(y)
    

for i in range(n2):
    arrasta(lista)

for i in lista:
    print(i,end=" ")



