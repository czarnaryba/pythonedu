from datetime import datetime

class Zadanie:
    def __init__(self, opis, priorytet, termin):
        self.opis = opis
        self.priorytet = priorytet
        self.termin = termin

    def __str__(self):
        return f"Zadanie: {self.opis}, Priorytet: {self.priorytet}, Termin: {self.termin}"

class MenedzerZadan:
    def __init__(self):
        self.zadania = []

    def dodaj_zadanie(self, zadanie):
        self.zadania.append(zadanie)

    def usun_zadanie(self, opis):
        for zadanie in self.zadania:
            if zadanie.opis == opis:
                self.zadania.remove(zadanie)
                return True
        return False

    def pokaz_zadania(self):
        if not self.zadania:
            print("Brak zadań do wyświetlenia.")
        else:
            for zadanie in self.zadania:
                print(zadanie)

def main():
    menedzer = MenedzerZadan()

    while True:
        print("\n1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Pokaż zadania")
        print("4. Wyjdź")

        wybor = input("Wybierz opcję (1-4): ")

        if wybor == '1':
            opis = input("Podaj opis zadania: ")
            priorytet = input("Podaj priorytet (Niski, Średni, Wysoki): ")
            termin_str = input("Podaj termin (yyyy-mm-dd): ")
            termin = datetime.strptime(termin_str, "%Y-%m-%d")
            zadanie = Zadanie(opis, priorytet, termin)
            menedzer.dodaj_zadanie(zadanie)
            print("Dodano zadanie.")
        
        elif wybor == '2':
            opis = input("Podaj opis zadania do usunięcia: ")
            if menedzer.usun_zadanie(opis):
                print("Usunięto zadanie.")
            else:
                print("Nie znaleziono zadania o podanym opisie.")
        
        elif wybor == '3':
            print("Lista zadań:")
            menedzer.pokaz_zadania()
        
        elif wybor == '4':
            print("Koniec programu.")
            break
        
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()

