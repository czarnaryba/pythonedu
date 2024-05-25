moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

nowa_lista = []

for element in moja_lista:
    if element not in nowa_lista:
        nowa_lista.append(element)

print("Lista tylko z unikalnymi elementami:")
print(nowa_lista)
