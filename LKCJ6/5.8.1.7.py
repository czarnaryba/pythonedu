def sprawdz_palindrom(wpisany_tekst):
    czysty_tekst = wpisany_tekst.replace(" ", "").lower()
    
    if czysty_tekst == czysty_tekst[::-1]:
        return "To jest palindrom"
    else:
        return "To nie jest palindrom"

dane_przykladowe = ["Ala wzory rozwala", "Ela wzory rozwala"]

for dane in dane_przykladowe:
    print(sprawdz_palindrom(dane))
