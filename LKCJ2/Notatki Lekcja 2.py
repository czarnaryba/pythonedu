print("Aye!")
#test
print("1")
print("2")

print("a","b","c", sep="\n")
print("a","b","c", sep="/")
print("linijka\n22")
#sep domyslnie spacja
#end dodaje cos na koncu oraz nie przechodzi do nowej linijki
print("a","b","c", sep="\n", end="!")
#end i sep zawsze na koncu
print("zaa", end=".")
print("zaa")
print("zaa")

#"napis" - typ danych string
# 10 - typ danych int integer, liczba calkowita
# 10.5 - typ danych float, liczba zmiennoprzecinkowa

print(10)
print(10.5)

print(0o123) #osemkowa
print(0x123) #szesnastkowa

print(3E8) #3 razy 10 do  potegi osmej

print()
print("uu")
print('apo poj')
print("'apo'")
print('"apko"')
print("apo \"3\"") # \ - znak ucieczki

# " s "
# "" d ""
# """ d """
##zrobic samemu poniżej

print('" samemu x3 "')

print(10 + 5) #znaki typu "+" to operator
# + - * /
# dzielenie daje float
print(2 ** 6) # potegowanie
print(11 // 5) #dzielenie calkowite
print(10 % 2) #modulo sprawdza ile razy 2 zmiesci sie 10
print(11 % 2) #modulo zwraca ile zostanie
print(-5) #liczba ujemna
print(+5) #liczba dodatnia
print(10 + 2 * 5)
print((10 + 2) * 5)
#potegowanie ponizej
print(3 ** 3 ** 3)
print(3 * 3 ** 3)
print(3 ** 3 * 3)
#> 10 wieksze od 2
print(10 > 11)
print(10 > 2)
#< 10 mniejsze od 2

#bcoolean, bool - True = 1, False = 0
print(True)
print(False)
print(True > False)
print(False > True)

zmienna = 5 ** 5 ** 2

print(zmienna)

#dopuszczalna zmienna_22 albo zmienna22
# musi sie zaczynac od litery lub _
a10 = 1
_a10 = 2
# nie moze sie zaczac od liczby i nie moze miec spacji
zmienna_druga = 10
#python rozpoznaje duze i male litery
#ZMIENNA_DRUGA nie bedzie dzialac jesli mamy zmienna_druga
print(zmienna_druga)

#zastrzezone nazwy
#sa w dokumentacji
#def = 11
#print(def)
definicja = 11
print(definicja)
#print(def)

#print(zmienna_trzecia)
#nie jest zdefiniowana

zmiennaString = "napis"
zmiennaInt = 10
zmiennaFloat = 10.1
zmiennaBool = True

print(zmiennaString, zmiennaInt, zmiennaFloat, zmiennaBool)

#nadpisywanie
zmiennaString = "zmiennaString inny napis"
print(zmiennaString)

zmiennaString = 2.0
print(zmiennaString, "zmiana na float")

zmiennaString = 2.0
#######print("str(zmiennaString) + "zmiana na float"")
#wrocic do teeeeeeeeeeego
#str zmienia typ danych na string

print(zmiennaInt + zmiennaString)

#str(dane) zmienia typ danych na string (napis
#int(dane) zmienia typ danych na integer (liczba)
#float(dane) zmienia typ danych na float (liczba po przecinku)

liczba = 2.2
print(float(liczba))
print(f"liczba jest rowna (liczba)")
      
wynik = 11 + 3
print(wynik)

wynik += 5
print(wynik)

wynik -= 1
print(wynik)

wynik *= 2
print(wynik)

wynik /= 3
print(wynik)

#celsjusz = int(input())
celsjusz = 10
kelwin = celsjusz + 273.15
fahremheit = (celsjusz * 9/5) + 32


print(f"Temperatura w celsjuszach to {celsjusz}")
print(f"Temperatura w kelwin to {kelwin}")
print(f"Temperatura w fahremheit to {fahremheit}")

#celsjusz = input()
#kelwin = int(celsjusz) + 273.15
#fahremheit = int(celsjusz) * 9/5) + 32

#imie = input("wpisz swoje imie")
#print(imie)

print("napis1" + "napis2")
print("napis1 " * 10)

#spacje
print("linijka\n")
print("linijka2")

print("linijka\n\n")
print("linijka2")
