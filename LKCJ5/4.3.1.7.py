def czy_przestepny(rok):
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    dlugosci_miesiecy = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if miesiac == 2 and czy_przestepny(rok):
        return 29
    else:
        return dlugosci_miesiecy[miesiac - 1]

testuj_lata = [1900, 2000, 2016, 1987]
testuj_miesiace = [2, 2, 1, 11]
testuj_wynik = [28, 29, 31, 30]
for i in range(len(testuj_lata)):
	r = testuj_lata[i]
	m = testuj_miesiace[i]
	print(r, m, "-> ", end="")
	wynik = dni_w_miesiacu(r, m)
	if wynik == testuj_wynik[i]:
		print("OK")
	else:
		print("Nie powiodło się")
