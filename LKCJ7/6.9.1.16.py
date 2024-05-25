def policz_i_zapisz(plik_wejsciowy):
    liczba_wystapien = {}

    try:
        with open(plik_wejsciowy, 'r', encoding='utf-8') as plik:
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

    sorted_liczba_wystapien = dict(sorted(liczba_wystapien.items(), key=lambda item: item[1], reverse=True))

    nazwa_pliku_hist = plik_wejsciowy.rsplit('.', 1)[0] + '.hist'  # Usunięcie rozszerzenia pliku wejściowego i dodanie ".hist"
    with open(nazwa_pliku_hist, 'w', encoding='utf-8') as plik_hist:
        for litera, ilosc in sorted_liczba_wystapien.items():
            plik_hist.write(f"{litera} -> {ilosc}\n")

nazwa_pliku = input("Podaj nazwę pliku: ")
policz_i_zapisz(nazwa_pliku)
