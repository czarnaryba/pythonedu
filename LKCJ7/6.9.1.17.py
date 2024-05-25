class NieprawidloweDaneWyjsciowe(Exception):
    pass

class PustyPlik(Exception):
    pass

class LiniaNiepoprawna(Exception):
    pass

class BrakPliku(Exception):
    pass

def suma_punktow_dla_ucznia(imie, nazwisko, punkty):
    return float(punkty)

def main():
    try:
        nazwa_pliku = input("Podaj nazwę pliku: ")
        suma_punktow = {}
        
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            for linia in plik:
                linia = linia.strip()
                if not linia:
                    raise PustyPlik("Plik jest pusty.")
                
                elementy_linii = linia.split()
                if len(elementy_linii)!= 3:
                    raise LiniaNiepoprawna("Linia nie ma trzech elementów.")
                
                imie, nazwisko, punkty = elementy_linii
                suma_punktow[(imie, nazwisko)] = suma_punktow.get((imie, nazwisko), 0) + suma_punktow_dla_ucznia(imie, nazwisko, punkty)
                
        for (imie, nazwisko), suma in sorted(suma_punktow.items(), key=lambda x: (-x[1], x)):
            print(f"{imie} {nazwisko} {suma:.1f}")
            
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
    except BrakPliku:
        print("Plik źródłowy istnieje, ale jest pusty.")
    except PustyPlik:
        print("Plik jest pusty.")
    except LiniaNiepoprawna:
        print("Linia nie ma trzech elementów.")
    except Exception as e:
        print(f"Niewłaściwe dane wejściowe: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
