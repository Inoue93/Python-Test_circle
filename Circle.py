import math

class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        if self.r <= 0:
            raise ValueError("Liczba jest za mała.")
        if (type(self.r) != float and type(self.r) != int):
            raise TypeError("Nie podano liczby")
        return math.pi * self.r ** 2

    def wypisz(self):
        print("Pole powierzchni wynosi:", self.pole())

p = Kolo(4)
p.wypisz()
l = Kolo(1)
l.wypisz()

