slowo_uzytkownika = input("Podaj słowo: ")

slowo_uzytkownika = slowo_uzytkownika.upper()

slowo_bez_samoglosek = ""

for litera in slowo_uzytkownika:
    # Uzupełnij pętlę for poniżej.
    if litera in "AEIOU":
        continue
    else:
        slowo_bez_samoglosek += litera
# Wyświetl słowo przypisane do zmiennej slowo_bez_samoglosek.
print(slowo_bez_samoglosek)