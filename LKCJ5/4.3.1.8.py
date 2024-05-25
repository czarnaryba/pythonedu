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

def dzien_w_roku(rok, miesiac, dzien):
    try:
        int(rok)
        int(miesiac)
        int(dzien)
    except ValueError:
        return None
    
    if rok < 1 or miesiac < 1 or miesiac > 12 or dzien < 1 or dzien > dni_w_miesiacu(rok, miesiac):
        return None
    
    return dzien

print(dzien_w_roku(2000, 12, 31)) 
print(dzien_w_roku(2000, 2, 29))  
print(dzien_w_roku(2000, 13, 1))   
print(dzien_w_roku(2000, 2, 30))   
print(dzien_w_roku(-1, 1, 1))    

