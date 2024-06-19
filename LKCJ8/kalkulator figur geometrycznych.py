import math

class Ksztalt:
    def pole(self):
        pass

class Kolo(Ksztalt):
    def __init__(self, promien):
        self.promien = promien
    
    def pole(self):
        return math.pi * (self.promien ** 2)

class Prostokat(Ksztalt):
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
    
    def pole(self):
        return self.szerokosc * self.wysokosc

class Trojkat(Ksztalt):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc
    
    def pole(self):
        return 0.5 * self.podstawa * self.wysokosc

kolo = Kolo(5)
prostokat = Prostokat(4, 6)
trojkat = Trojkat(3, 7)

print("Pole koła o promieniu 5:", kolo.pole())
print("Pole prostokąta o wymiarach 4x6:", prostokat.pole())
print("Pole trójkąta o podstawie 3 i wysokości 7:", trojkat.pole())
