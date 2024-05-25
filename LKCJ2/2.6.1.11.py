h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

# wprowadź tutaj swój kod

suma = m + d #suma minut
godzinyAdd = suma // 60
minuty = suma % 60
h = (h + godzinyAdd) % 24

print(h, ":", minuty, sep='')
