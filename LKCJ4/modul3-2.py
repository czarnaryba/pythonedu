lista = [1,3,4,1.3,"napis",True,False]
print(lista)
print(lista[3])
lista.append(90)
lista.insert(1, "element")
print(lista)
del lista[-1]
print(lista)

#del lista
#print(lista)

print(len(lista))

#nazwaListy.nazwaMetody(argumenty) #metoda
#nazwaFunkcji(argumenty) #funkcja

pusta = []
print(pusta)

for i in range(5):
    pusta.insert(0, i+1)

print(pusta)

#for i in pusta:
#    print(i)

for i in range(len(pusta)):
    indeks = -(i+1)
    print(pusta[indeks])

suma = 0
for i in pusta:
    suma = suma + i
print(suma)

zmienna = pusta[0]
pusta[0] = pusta[1]
pusta[1] = zmienna
print(pusta)

pusta[0], pusta[1] = pusta[1], pusta[0]
print(pusta)

lista_1 = [1]
lista_2 = lista_1
lista_1[0] = 2
print(lista_2)

#zmienna_1 = 1
#zmienna_2 = zmienna_1
#zmienna_1 = 2
#print(zmienna_2)

lista_1 = [1]
lista_2 = lista_1[:]
lista_1[0] = 2
print(lista_2)

print(pusta[1:4]) #od:do
print(pusta[:]) #całość listy
print(pusta[1:-1]) #1:4
print(pusta[1:4:2]) #od:do co drugi
print(pusta[:4]) #0:4
print(pusta[3:]) #3:len(lista)
print(pusta[3:len(lista)]) #3:5

del pusta[2:4]
print(pusta)

del pusta[:]
print(pusta)

for i in range(1,11):
    pusta.append(i)
print(pusta)

print(12 in pusta)
print(6 in pusta)
print(12 not in pusta)
print(6 not in pusta)

if 10 in pusta:
    print("liczba istnieje")

pusta = [3, 6, -2, 20, 3, 0, 10]

najwieksza = 0
for elem in pusta:
    if elem > najwieksza:
        print("liczba jest większa", najwieksza, elem)
        najwieksza = elem
    else:
        print("liczba jest mniejsza", najwieksza, elem)
print(najwieksza)

print(max(pusta))

lista2d = [[1,2,3],[4,5,6],[7,8,9]]
print(lista2d)
print(lista2d[0])
print(lista2d[0][2])
lista2d[0] = [3,2,1]
print(lista2d)
lista2d[0] = [1,2,3,4,5]
print(lista2d)
lista2d[0] = True
print(lista2d)

lista2d[0] = [1,2,3]
print(lista2d)

for elem in lista2d:
    for elem2 in elem:
        print(elem2)
        print("wykonanie drugiej pętli")
    print("wykonanie pierwszej pętli")

nowa2d = []
for i in range(10):
    tmp = []
    for j in range(5):
        tmp.append(j)
    nowa2d.append(tmp)
    print(nowa2d[i])

#print(nowa2d)

jednowymiarowa = []
for i in range(10):
    jednowymiarowa.append(i)
print(jednowymiarowa)

jednowymiarowa = [i for i in range(10)]
print(jednowymiarowa)

nowa2d = []
for i in range(10):
    tmp = [j for j in range(5)]
    nowa2d.append(tmp)
    print(nowa2d[i])

print()

nowa2d = [[j for j in range(5)] for i in range(10)]

for e in nowa2d:
    print(e)

nowa3d = [[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]]
#print(nowa3d)

for e in nowa3d:
    print()
    for e2 in e:
        print(e2)
        
print("koniec for")
print(nowa3d[0])
print(nowa3d[0][0])
print(nowa3d[0][0][0])
print(nowa3d[2][2][2])

for e in nowa3d:
    for e2 in e:
        for e3 in e2:
            print(e3)

nowa3d = []
for i in range(5):
    tmp = []
    for j in range(5):
        tmp2 = []
        for k in range(5):
            tmp2.append(k)
        tmp.append(tmp2)
        print(tmp2)
    nowa3d.append(tmp)
    print()

nowa3d = [[[k for k in range(5)] for j in range(5)] for i in range(5)]
for e in nowa3d:
    print()
    for e2 in e:
        print(e2)

lista = []

liczbaElem = int(input("Wprowadź liczbę elementów w liście: "))

for i in range(liczbaElem):
    wartosc = int(input("Wpisz liczbę: "))
    lista.append(wartosc)

print(lista)

nieposortowane = True
while nieposortowane:
    nieposortowane = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            nieposortowane = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(lista)

#wykonać wszystkie laby z rozdziałów 3.4, 3.6. Dodatkowo należy zrobić quiz oraz test z modułu 3
