def dziel(liczba, liczba2):
    try:
        wynik = liczba / liczba2
    except ZeroDivisionError:
        print("Nie można dzielić przez 0")
        wynik = 0
    else:
        print("Wszystko OK")
    finally:
        print("Koniec")

    return wynik

print(dziel(10,2))
print(dziel(10,0))


try:
    i = int("napis")
except Exception:
    print("znaleziono błąd")

try:
    i = int("napis")
except Exception as zmienna:
    print(zmienna)
    print(zmienna.__str__())



class MojWyjatekError(ZeroDivisionError):
    pass

def dziel(liczba, liczba2):
    if liczba2 == 1:
        raise MojWyjatekError("Nie można dzielić przez 1")
    
    
    wynik = liczba/liczba2
    return wynik

try: 
    print(dziel(10,2))
    print(dziel(10,1))
except ZeroDivisionError:
    print("błąd, zero division")
except MojWyjatekError:
    print("błąd")


class bazowyError(Exception):
    def __init__(self, wiadomosc = "brak"):
        Exception.__init__(self, wiadomosc)

class podrzednyError(bazowyError):
    def __init__(self, wiadomosc = "brak", liczba = 0):
        bazowyError.__init__(self, wiadomosc)
        self.liczba = liczba
        print(self.liczba)

def funkcja(napis):
    if len(napis) > 10:
        raise podrzednyError("za długi napis", len(napis))

#funkcja("1234")
#funkcja("123467891011")

lista = [x for x in range(0,11)]
print(lista)

for element in range(0,6):
    print(element)

class MojGenerator:
    def __init__(self, liczba):
         self.granica = liczba
         self.liczba = 0

    def __iter__(self):
        print("iter")
        return self

    def __next__(self):
        print("next")
        self.liczba += 1
        if self.liczba > self.granica:
            raise StopIteration
        return self.liczba

for element in MojGenerator(10):
    print(element)
    wynik = element ** 2
    print(wynik)

def petla(liczba):
    for i in range(liczba):
        return i
    
def petla2(liczba):
    for i in range(liczba):
        yield i

print(petla(10))
for element in petla2(10):
    print(element)

lista = []
for x in range(10):
    #if x % 2 == 0:
    #    lista.append(1)
    #else:
    #    lista.append(0)
    lista.append(1 if x % 2 == 0 else 0)
print(lista)

#wynik jeżeli warunek jeżeli_nie inny_wynik 
print(10 if 2 > 3 else 1)

z = lambda:2
print(z)
print(z())

#lambda parametry: wynik
kwadrat = lambda x: x * x
for element in range(1,5):
    print(kwadrat(element))

potega = lambda x,y: x ** y
print(potega(2,5))

m = map(lambda x: 2**x, lista)
lista2 = list(m)
print(m)
for e in map(lambda x: 2**x, lista):
    print(e)

print(lista2)

filtr = list(filter(lambda x: x < 1, lista))
print(filtr)

def z(x):
    y = x

l = 1
z(l)

print(l)
#print(y)

def z(x):
    y = x

    #def w():
    #    return y
    def w(potega):
        return y ** potega

    return w

l = 2
wynik = z(l)
print(wynik(4))

# C:\\folder\\plik
# /folder/plik

# r - tryb odczytu, plik musi istnieć
# w - tryb zapisu, plik nie musi istnieć
# a - tryb dopisywania, plik nie musi istnieć
# r+ - odczyt i aktualizacja, plik musi istnieć
# w+ - zapis i aktualizacja, plik nie musi istnieć
# rt, rb
# r+t, r+b

try:
    strumien = open("tekst.txt", "r", encoding = "utf-8")
    #print(strumien.read())
    print(strumien.read(10))
    strumien.close()
except Exception as e:
    print(e)


strumien = open("zdania.txt", "r", encoding = "utf-8")
print(strumien.readline(), end="")
print(strumien.readline(), end="")
print(strumien.readline(), end="")
print(strumien.readline())
strumien.close()

strumien = open("zdania.txt", "r", encoding = "utf-8")
lista = strumien.readlines()
print(lista)
print(lista[0])
strumien.close()

zapis = open("zapis.txt", "w", encoding = "utf-8")
zapis.write("coś zapisałam\ndalsze dane")
zapis.write("coś nowego")
zapis.close()

aktualizacja = open("zapis.txt", "a", encoding = "utf-8")
aktualizacja.write("\nnowa zawartość po aktualizacji")
aktualizacja.close()

odczytA = open("zapis.txt", "r+", encoding = "utf-8")
print(odczytA.read())
odczytA.write("nowe dane")
odczytA.close()

# ścieżka absolutna
# C:\Users\Użytkownik\OneDrive\Desktop
#
# ścieżka relatywna do folderu xyz
# "xyz\zapis.txt"
#
# 
#

#import sys

#stdin - standard input, związany z input()
#stdout - standard output, zwiąnay z print()
#stderr - error ouput

#należy zrobić laboratorium 6.9.1.16, 6.9.1.17, 6.9.1.15
#oraz test podsumowujący z części 2 kursu
