rok = int(input("Wprowadź rok: "))

if rok < 1582:
    print("Nie ma tego roku w kalendarzu gregoriańskim.")
else:
    if rok % 4 == 0:
        if rok % 100 == 0:
            if rok % 400 == 0:
                print("Rok przestępny")
            else:
                print("Rok zwykły")
        else:
            print("Rok przestępny")
    else:
        print("Rok zwykły")
