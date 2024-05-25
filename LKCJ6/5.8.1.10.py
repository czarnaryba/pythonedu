def czy_schronione(pierwszy, drugi):
    pierwszy = pierwszy.lower()
    drugi = drugi.lower()
    
    return pierwszy in drugi

dane_testowe = [
    ("motyw", "lokomotywownia"),
    ("motyl", "lokomotywownia")
]

for dane in dane_testowe:
    wynik = czy_schronione(*dane)
    print(f"{wynik}")
