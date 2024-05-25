def policz_litery(plik_sciezka):
    liczba_wystapien = {}

    try:
        with open(plik_sciezka, 'r', encoding='utf-8') as plik:
            tresc_pliku = plik.read().lower()  
            for znak in tresc_pliku:
                if znak.isalpha():  
                    if znak in liczba_wystapien:
                        liczba_wystapien[znak] += 1
                    else:
                        liczba_wystapien[znak] = 1
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return

    for litera, ilosc in sorted(liczba_wystapien.items()):
        print(f"{litera} -> {ilosc}")

nazwa_pliku = input("Podaj nazwę pliku: ")
policz_litery(nazwa_pliku)
