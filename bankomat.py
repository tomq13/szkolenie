class Bankomat():

    def __init__(self):
        self.__saldo = 5000
        self.__logowanie = 0
        self.__status = 0

    def logowanie(self, pin):
        self.__pin = pin
        if self.__pin != 1234:
             self.__logowanie += 1
             self.__status = 0
        else:
             self.__logowanie = 0
             self.__status = 1
        return self.__logowanie


    def wplata(self, kwota_wpl):
        if self.__status == 1:
            self.__saldo += kwota_wpl
            print(f"Saldo po operacji wynosi {self.__saldo}")


    def wyplata(self, kwota_wypl):
        if self.__status == 1:
            if kwota_wypl > self.__saldo:
                print("Podana kwota przewyższa saldo na rachunku")
            else:
                self.__saldo -= kwota_wypl
                print(f"Saldo po operacji wynosi {self.__saldo}")


    def saldo(self):
        if self.__status == 1:
            print(f"Saldo rachunku wynosi: {self.__saldo}")


s = Bankomat()


while True:
    pin = int(input("Podaj PIN"))
    log = s.logowanie(pin)
    if log == 3:
        print("Przekroczono liczbę prób. Karta została zablokowana")
        break
    elif log != 0:
        print("Błędny pin. Prosze spróbować jeszcze raz")
    else:
        wybor = int(input("""Wybór operacji:
           1. Wpłata
           2. Wypłata
           3. Saldo
           4. Koniec
           """))

        if wybor == 1:
            wplata = float(input("Podaj kwotę: "))
            s.wplata(float(wplata))
        elif wybor == 2:
            wyplata = float(input("Podaj kwotę: "))
            s.wyplata(float(wyplata))
        elif wybor == 3:
            s.saldo()
        else:
            break