def nazwa_funkcji():
    print("funkcja wywołana")
    print("kolejna wiadomość")
    print("koniec funkcji")

nazwa_funkcji()
print("rozpoczęcie naszego programu")
nazwa_funkcji()
print("koniec programu")
nazwa_funkcji()
nazwa_funkcji()

#
#
#

def wypisz_wiadomosc():
    print("Witaj świecie")

wypisz_wiadomosc()

def wypisz_wiadomosc():
    print("Hello world")

wypisz_wiadomosc()

wypisz_wiadomosc = 1 #tak nie robimy
print(wypisz_wiadomosc) #

#
#

def wypisz_imie():
    print("Jestem Jan")

wypisz_imie()

def przedstaw_sie(imie):
    #imie = "coś"
    print("Mam na imie",imie)

def przedstaw_sie(imie, nazwisko):
    #imie = "coś"
    print("Mam na imie " + str(imie) + " " + str(nazwisko))

przedstaw_sie(1, 2)

przedstaw_sie("Ania", "Kowalska")
przedstaw_sie("Kowalska", "Ania")

argument_imie = "Adam"
argument_nazwisko = "Nowak"
przedstaw_sie(argument_imie, argument_nazwisko)
print(argument_imie, argument_nazwisko)

przedstaw_sie(nazwisko = "Kowalska", imie = "Ania")

def suma(a, b, c, d):
    print(a + b + c + d)

suma(1,2,3,4)
suma(a = 1, b = 2, c = 3, d = 4)
suma(d = 4, b = 2, a = 1, c = 3)
suma(1,2, d = 4, c = 3)
#suma(d = 4, 1, 2, 3) źle
#suma(a = 1, b = 2, c = 3, d = 4, e = 5) źle

def iloczyn(a, b = 2):
    print(a * b)

print("wywołanie normalne")
iloczyn(1, 2)
iloczyn(10, 2)
iloczyn(5, 2)
print("argument domyślny")
iloczyn(1) # iloczyn(1,2)
iloczyn(10)
iloczyn(5)

iloczyn(5, 3)

iloczyn(a = 6)

def roznica(a = 0, b = 0):
    print(a - b)
    #return
    #return None

roznica()
roznica(a = 2)
roznica(b = 3)
roznica(4, 5)

def odliczanie(zyczenia = True):
    print("trzy")
    print("dwa")
    print("jeden")

    if zyczenia == False:
        return

    print("wszystkiego najlepszego")

odliczanie()
odliczanie(False)

def dzielenie(a,b):
    return a/b

print(dzielenie(3,3))

wynik = dzielenie(10,2) # wynik = 5.0
print(wynik)

def oblicz(a,b):
    wynik = (a + b) * 2
    print("obliczono")
    return wynik

oblicz(2,3)
print(oblicz(2,3))
print(roznica(3,3))

pusta = None
print(pusta)
#print(pusta + 2)
#pusta = 3
#print(pusta)

if pusta == None:
    print("zmienna jest pusta")
else:
    print("zmienna posiada wartość")

if iloczyn(2,2) == None:
    print("funkcja nic nie zwraca")
else:
    print("funkcja zwraca wynik")

def sprawdz_parzystosc(liczba):
    if liczba % 2 == 0:
        return True
    return False

print(sprawdz_parzystosc(4))
print(sprawdz_parzystosc(3))

def dodaj_do_listy(lista):
    lista.append(10)

lista = [1,2,3,4,5]
print(lista)
dodaj_do_listy(lista)
print(lista)

def funkcja():
    #lokalna
    x = 10
    print(x)
    #return x

funkcja()
#print(x)

#globalna
y = "hej"

def powitaj():
    print(y)

powitaj()

wiadomosc = "witaj"
globalna = 1

def powitaj2():
    global wiadomosc, globalna
    #global globalna
    wiadomosc = "żegnaj"
    globalna += 1
    print(wiadomosc)

print(wiadomosc, globalna)
powitaj2()
print(wiadomosc, globalna)

# 1
# 1
# 2
# 3
# 5
# 8
# 13

def fib(ilosc):
    suma = 0
    element1 = 1
    element2 = 1

    if ilosc < 0:
        return
    if ilosc < 3:
        return 1
    
    for i in range(3, ilosc+1):
        suma = element1 + element2
        element1 = element2
        element2 = suma
    return suma

for n in range(1,10):
    print(fib(n))

def rekurencja(licznik = 0):
    print("rekurencja")
    licznik += 1

    if licznik > 5:
        return
    
    rekurencja(licznik)

rekurencja()

def fib_r(ilosc):
    if ilosc < 0:
        return
    if ilosc < 3:
        return 1

    #           3 - 1 = 2   +  3 - 2 = 1
    #               1       +     1  = 2

    #               2       +        1 = 3
    return fib_r(ilosc - 1) + fib_r(ilosc - 2)

for n in range(1,10):
    print(fib(n))

#Dla tych co, chcą jeszcze potrenować funkcje:
#Labki z netacada, tylko z funkcji, moduł 4

#Dla chętnych:
#stwórzcie funkcję do obliczania bmi. Zabiecz funkcję przed złymi wartościami (stringi, zbyt duży wzrost/waga, minusowy wzrost/waga, dzielenie przez 0)
#stwórz funkcję do sprawdzenia czy na podstawie 3 boków da się stworzyć trójkąt prostokątny.
#funkcja obliczająca silnię. Dwie wersje, pętla, oraz rekurencja.

