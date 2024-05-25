tajny_numer = 777

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
twoj_numer = int(input("Wprowadź numer: "))

while twoj_numer != tajny_numer:
    print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")
    twoj_numer = int(input("Wprowadź numer: "))

print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
