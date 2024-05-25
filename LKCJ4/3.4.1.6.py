liczby_z_kapelusza = [1, 2, 3, 4, 5]  # Istniejąca lista liczb ukrytych w kapeluszu.

# Krok 1: Napisz wiersz kodu, który prosi użytkownika
# o zastąpienie środkowego numeru liczbą całkowitą wprowadzoną przez użytkownika.
liczby_z_kapelusza[2] = int(input("Wprowadź nową środkową liczbę: "))

# Krok 2: Napisz tutaj wiersz kodu, który usuwa ostatni element z listy.
del liczby_z_kapelusza[4]

# Krok 3: Napisz tutaj wiersz kodu, który wypisuje długość istniejącej listy.
print("Długość listy: " + str(len(liczby_z_kapelusza)))

print(liczby_z_kapelusza)  # Wyświetlanie zawartości listy.
