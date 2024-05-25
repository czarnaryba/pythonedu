# Krok 1
beatles = []
print("Krok 1:", beatles)

# Krok 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Krok 2:", beatles)

# Krok 3
for i in range(2):
    new_member = input("Wprowadź nazwę nowego członka zespołu: ")
    beatles.append(new_member)
print("Krok 3:", beatles)

# Krok 4
del beatles[-2]
del beatles[-1]
print("Krok 4:", beatles)

# Krok 5
beatles.insert(0, "Ringo Starr")
print("Krok 5:", beatles)


# Sprawdzanie długości listy.
print("The Fab", len(beatles))

