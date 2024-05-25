representacje_cyfr = {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###')
}

def wyświetl_cyfre(cyfry):
    cyfry_str = str(cyfry)
    for cyfra in cyfry_str:
        for linia in representacje_cyfr[cyfra]:
            print(linia)
        print()

wyświetl_cyfre(123)
print("\n")
print("\n")
print("\n")
print("\n")
wyświetl_cyfre(9081726354)
