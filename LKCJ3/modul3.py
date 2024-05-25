print(2 == 2)
print(2 == 3)

zmienna = 5.5
zmienna2 = 10.5
print(5.5 == zmienna2) #5.5 == 10.5
print(zmienna == zmienna2) #5.5 == 10.5
print(zmienna == 10.5) #5.5 == 10.5

var = 5
print((10 / 2) == (var * 2))

print(2 != 2)
print(2 != 3)

trojka = 3
piatka = 5
print(trojka > piatka)
print(trojka < piatka)
print(trojka >= piatka)
print(trojka <= piatka)
print(trojka >= 3)
print(trojka <= 3)

#if (prawda lub fałsz):
#    kawałek kodu do zrobienia
#    kolejna linijka
#    jeszcze kolejna
#kontynuacja kodu

#n = int(input("Podaj liczbe n: "))
#print(n >= 100)
#if (n >= 100):
 #   if n == 100:
  #      print("n jest równe 100")
   # else:
   #     print("n jest większe od 100")
#elif n == 50:
 #   print("n jest równe 50")
#elif n == 1:
 #   print("n jest równe 1")
#else:
 #   print("n jest większe od 1 i mniejsze od 100")

licznik = 0
while licznik <= 10:
    print("x jest mniejsze od 10")
    licznik = licznik + 1

while licznik != 0:
    print("zmniejszamy wartość")
    licznik = licznik - 1 
else:
    print("wykonano else")

for i in range(11):
    print("wykonał się for")
    print(i)
    
for licznik2 in range(5,11):
    print("wykonał się for")
    print(i)

for j in range(10, 21, 2):
    print("przejscie co 2 cyfry")
    print(j)

#break
#continue
#pass

for q in range(1, 11):
    if q == 5:
        break
    print(q)

for q in range(1, 11):
    if q == 5:
        continue
    print(q)
else:
    print("koniec for")

#wyjscie = 0
#while True:
 #   liczba = input("Podaj liczbe: ")
  #  if int(liczba) == 0:
   #     break
   # print(int(liczba) / 2)

#if jakiś warunek:
#    pass

#boolean - True lub False
#bool

#zapis = int(input("wpisz liczbe: "))
#print(zapis < 10)
#warunek = zapis < 10 #zmienna o typie bool
#print(warunek)

#and - i, koniukcja, iloczyn logiczny (&)
# operator 1   operator 2   wynik
#     True          True    True
#     True          False   False
#     False         False   False
#     False         True    False
#or - lub, alternatywa, suma logiczna (|)
# operator 1   operator 2   wynik
#     True          True    True
#     True          False   True
#     False         False   False
#     False         True    True
#not - przeciwność, negacja (~)
# operator 1   wynik 
#     True      False 
#     False     True

#if zapis > 10:
#    if zapis < 15:
#        print("liczba jest większa od 10 i mniejsza od 15")

#print(zapis > 10 and zapis < 15)
#if zapis > 10 and zapis < 15:
 #   print("liczba jest większa od 10 i mniejsza od 15")

#if zapis > 10 or zapis < 15:
#    print("liczba jest większa od 10 lub mniejsza od 15")

#print(not warunek)

#(jakiś warunek or kolejny warunek) and trzeci warunek
#warunek or not(warunek2 and warunek3)

lista = [1,2,3,4,5]
print(lista)
print(lista[1])
print(lista[0])
liczbaZListy = lista[0]
print(liczbaZListy)
lista[4] = 10
print(lista[4])
print(lista)
print(lista[2-1])
zmienna = 10
print(lista[zmienna - zmienna])

print("początek for")
licznik = 0
for element in lista:
    if licznik == 0 or licznik == len(lista) - 1:
        licznik += 1
        continue
    licznik += 1 #licznik = licznik + 1
    print(element)

print(lista[1:4]) #od:do
print(lista[1:4:2]) #od:do:krok
print("len", len(lista))
print(lista[-1])
print(lista[-2])

del lista[2]
print(lista)
print(len(lista))

#print(lista[6])

lista = [1,2,3,4,5]
lista[2] = "none"
print(lista)
for i in lista:
    if i != "none":
        print(i)

lista.append(100)
print(lista)

lista.insert(1, 200)
print(lista)

print("koniec programu")

#jako zadanie zrobić wszystkie laboratoria z rozdziałów 3.1 i 3.2 w module 3
