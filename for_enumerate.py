#fOR

print("\n Utilizando a função range() com len()")
lista = [1,2,3,4,5]
for indice in range(0, len(lista)):
    print("Nosso Indice:", indice)
    print("Nosso Elemento:", lista[indice])
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

#Enumerate / enumerate()
lista_enumerate = ["a", "b","c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")
