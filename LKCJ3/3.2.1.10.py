slowo_uzytkownika = input("Wprowadź słowo: ") # Poproś użytkownika o wprowadzenie słowa
slowo_uzytkownika = slowo_uzytkownika.upper() # i przypisz je do zmiennej slowo_uzytkownika

for litera in slowo_uzytkownika:
    # Uzupełnij pętlę for poniżej.
    if litera in "AEIOU":
        continue
    print(litera)