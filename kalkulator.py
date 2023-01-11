from kalkulator import funkcje

while True:
    wybor = int(input("""Wybierz rodzaj obliczeń:
    1. Sumowanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Wyjście
    """))

    if wybor == 5:
        break
    elif wybor < 5:
        a = float(input("a = "))
        b = float(input("b = "))

        if wybor == 1:
            print("Suma liczb wynosi: ", funkcje.suma(a, b))
        elif wybor == 2:
            print("Różnica liczb wynosi: ", funkcje.roznica(a, b))
        elif wybor == 3:
            print("Iloczyn liczb wynosi: ", funkcje.iloczyn(a, b))
        else:
            if b == 0:
                print("Nie można dzielić przez 0!")
            else:
                print("Iloraz liczb wynosi: ", funkcje.iloraz(a, b))
    else:
        print("Proszę wybrać liczbę z zakresu 1 - 5")