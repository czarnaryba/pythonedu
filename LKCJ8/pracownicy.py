from datetime import datetime

class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, pensja, data_zatrudnienia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.pensja = pensja
        self.data_zatrudnienia = data_zatrudnienia

    def __str__(self):
        return (f"Imię: {self.imie}, Nazwisko: {self.nazwisko}, "
                f"Stanowisko: {self.stanowisko}, Pensja: {self.pensja}, "
                f"Data zatrudnienia: {self.data_zatrudnienia}")

class MenedzerPracownikow:
    def __init__(self):
        self.pracownicy = []

    def dodaj_pracownika(self, pracownik):
        self.pracownicy.append(pracownik)

    def usun_pracownika(self, kryterium):
        do_usuniecia = [prac for prac in self.pracownicy 
                        if kryterium.lower() in prac.imie.lower() or kryterium.lower() in prac.nazwisko.lower()]
        if not do_usuniecia:
            print("Nie znaleziono pracownika.")
            return

        if len(do_usuniecia) > 1:
            print("Znaleziono kilku pracowników:")
            for idx, prac in enumerate(do_usuniecia):
                print(f"{idx + 1}. {prac}")
            wybor = int(input("Podaj numer pracownika do usunięcia: ")) - 1
            self.pracownicy.remove(do_usuniecia[wybor])
        else:
            self.pracownicy.remove(do_usuniecia[0])
        print("Pracownik został usunięty.")

    def edytuj_pracownika(self, kryterium):
        do_edycji = [prac for prac in self.pracownicy 
                     if kryterium.lower() in prac.imie.lower() or kryterium.lower() in prac.nazwisko.lower()]
        if not do_edycji:
            print("Nie znaleziono pracownika.")
            return

        if len(do_edycji) > 1:
            print("Znaleziono kilku pracowników:")
            for idx, prac in enumerate(do_edycji):
                print(f"{idx + 1}. {prac}")
            wybor = int(input("Podaj numer pracownika do edycji: ")) - 1
            pracownik = do_edycji[wybor]
        else:
            pracownik = do_edycji[0]

        print("Wprowadź nowe dane (pozostaw puste, aby nie zmieniać):")
        imie = input(f"Imię ({pracownik.imie}): ") or pracownik.imie
        nazwisko = input(f"Nazwisko ({pracownik.nazwisko}): ") or pracownik.nazwisko
        stanowisko = input(f"Stanowisko ({pracownik.stanowisko}): ") or pracownik.stanowisko
        pensja = input(f"Pensja ({pracownik.pensja}): ") or pracownik.pensja
        data_zatrudnienia = input(f"Data zatrudnienia ({pracownik.data_zatrudnienia}): ") or pracownik.data_zatrudnienia

        pracownik.imie = imie
        pracownik.nazwisko = nazwisko
        pracownik.stanowisko = stanowisko
        pracownik.pensja = pensja
        pracownik.data_zatrudnienia = data_zatrudnienia

        print("Dane pracownika zostały zaktualizowane.")

    def pokaz_pracownikow(self):
        if not self.pracownicy:
            print("Brak pracowników do wyświetlenia.")
        else:
            for pracownik in self.pracownicy:
                print(pracownik)

def main():
    menedzer = MenedzerPracownikow()

    while True:
        print("\n1. Dodaj pracownika")
        print("2. Edytuj pracownika")
        print("3. Usuń pracownika")
        print("4. Wyświetl pracowników")
        print("5. Zakończ")

        wybor = input("Wybierz opcję (1-5): ")

        if wybor == '1':
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            stanowisko = input("Podaj stanowisko: ")
            pensja = input("Podaj pensję: ")
            data_zatrudnienia = input("Podaj datę zatrudnienia (yyyy-mm-dd): ")
            pracownik = Pracownik(imie, nazwisko, stanowisko, pensja, data_zatrudnienia)
            menedzer.dodaj_pracownika(pracownik)
            print("Dodano pracownika.")

        elif wybor == '2':
            kryterium = input("Podaj imię lub nazwisko pracownika do edycji: ")
            menedzer.edytuj_pracownika(kryterium)

        elif wybor == '3':
            kryterium = input("Podaj imię lub nazwisko pracownika do usunięcia: ")
            menedzer.usun_pracownika(kryterium)

        elif wybor == '4':
            print("Lista pracowników:")
            menedzer.pokaz_pracownikow()

        elif wybor == '5':
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
