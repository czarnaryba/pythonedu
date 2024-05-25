import math
import sys

#import math, sys

print(math.pi)
print(math.sin(2))

pi = 3.14
print(pi)

from math import cos

#print(pi)

pi = 19

#print(pi)
#print(cos(pi))

####

i = 0
i += 1
print(i)

import math

print(math.sin(i))

###

from math import *

print(pi)
print(sin(2))
print(cos(3))

###

import math as m

#print(m.pi)
#print(m.cos(2))
#print(m.ceil(3.12232))

###

from math import ceil as zaokraglij, pi as p

#print(zaokraglij(0.99999))
#print(p)

###

#print(dir(math))

###

from random import random, seed, randrange, randint

print("liczby losowe")

#seed(10)
for i in range(10):
    print(random())

print(randrange(0,10))
print(randint(0,10))

if randint(0,1) == 0:
    print("liczba jest 0")
else:
    print("liczba jest 1")

###

import platform

print(platform.platform())
print(platform.machine())
print(platform.processor())
print(platform.system())

###

lista = ['j', 'e', 's', 't', 'e', 'm']
lancuch = "jestem łańcuchem znaków!"
print(lancuch)

print(len(lista))
print(len(lancuch))

for e in lista:
    print(e)

for e in lancuch:
    print(e)

print(lista[2])
print(lancuch[2])

print(lista[1:3])
print(lancuch[1:3])

print('j' in lista)
print('j' in lancuch)

del lista[0]
lista.append("10")
print(lista)

#lancuch.append("10")
#print(lancuch)

kilkaLinijek = "pierwsza linijka\ndruga linijka\ntrzecia linijka\nczwarta"

lancuch = """pierwsza linijka
druga linijka
trzecia linijka
czwarta"""

print(kilkaLinijek)
print(lancuch)

a = "jestem"
b = "Python"

print(a + b)

wynik = a + b
print(wynik, a, b)
print(wynik + "1")

#kopia = wynik + "1"
#wynik = kopia

wynik += "1"
print(wynik)

print(wynik * 4)
print("a" * 10)

#kopia = wynik * 2
#wynik = kopia

wynik *= 2
print(wynik)

print(ord("g"))
print(ord("G"))
print(ord(" "))

kody = []
#print(ord(wynik))
for e in wynik:
    print(ord(e), end="")
    kody.append(ord(e))
print(kody)

print("\n")
print(chr(120))
print(chr(200))
print(chr(300))
print(chr(500))

napis = ""
for e in kody:
    napis += chr(e)
print(napis)

print(ord("1"))

print(min(napis))
napis = "BASUicu@zxuihz@iSjdhIAUSL"
print(min(napis))
print(max(napis))

print(napis.index("@"))
print(napis[napis.index("L")])

listaNapis = list(napis)
print(listaNapis)
print(napis.count("@"))
print(napis.capitalize())
print(napis.upper())
print(napis.lower())

print("s" < "S")
print("python" < "Python")
print("python" == "Python")
print("python" == "python")
print("10" > "010")

###
try:
    #wynik = 2/0
    #wynik = 1 + "kjl"
    x = int(input("wprowadz liczbe"))
    print(x/2)
except ZeroDivisionError:
    print("Błąd! Dzielenie przez zero")
except TypeError:
    print("Błąd typu!")
except ValueError:
    print("Błąd! Wpisz liczbę")
except: 
    print("Błąd!")


print("dalsze wykonywanie")

#lab 5.7, 5.11,
#lab 5.8.1.7, 5.8.1.8, 5.8.1.10
#dla chętnych 5.8.1.6, 5.8.1.9, 5.8.1.11
