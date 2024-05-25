def readint(prompt, min, max):
    while True:
        wprowadzona = input(prompt)
        try:
            liczba = int(wprowadzona)
            if min <= liczba <= max:
                return liczba
            else:
                print("Błąd: podana liczba jest spoza dozwolonego zakresu ({},{}).".format(min, max))
        except ValueError:
            print("Błąd: wprowadzono nieprawidłową liczbę.")

v = readint("Podaj liczbe od -10 do 10: ", -10, 10)
print("Liczba to:", v)
