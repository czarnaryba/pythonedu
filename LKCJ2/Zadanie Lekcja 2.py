km = float(input("Wprowadź odległość podaną w kilometrach: "))

metry = km * 1000 
mili =  metry * 1000
centy = metry * 100
cale = metry * 39.3700787
stopy = metry * 3.2808399
mile = metry * 0.000621371192

print(str(km) + " to " + str(mili) + " milimetry")
print(str(km) + " to " + str(centy) + " centymetry")
print(str(km) + " to " + str(metry) + " metry")
print(str(km) + " to " + str(cale) + " cale")
print(str(km) + " to " + str(stopy) + " stopy")
print(str(km) + " to " + str(mile) + " mile")
