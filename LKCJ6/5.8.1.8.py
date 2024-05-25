def sprawdz_anagramy(wyraz1, wyraz2):
    wyraz1 = wyraz1.replace(" ", "").lower()
    wyraz2 = wyraz2.replace(" ", "").lower()

    if wyraz1 == "" or wyraz2 == "":
        return "to nie anagramy."

    if len(set(wyraz1)) == len(set(wyraz2)):
        return "to anagramy."
    else:
        return "to nie anagramy."

dane_testowe1 = [
    ("arbuzy", "burza")
]

dane_testowe2 = [
    ("Ranek", "Nerka")
]

for dane in dane_testowe1:
    wynik = sprawdz_anagramy(*dane)
    print(f"{dane} {wynik}")

for dane2 in dane_testowe2:
    wynik = sprawdz_anagramy(*dane2)
    print(f"{dane2} {wynik}")
