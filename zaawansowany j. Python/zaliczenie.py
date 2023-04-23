# Zadanie 1
class Time:
    hour = 0
    minute = 0

    def add_two_times(first_time, second_time):
        new_hour = first_time.hour + second_time.hour
        new_minute = first_time.minute + second_time.minute

        if new_minute >= 60:
            new_minute = new_minute - 60
            new_hour = new_hour + 1

        if new_hour >= 24:
            new_hour = new_hour - 24
        return Time(new_hour, new_minute)

    def is_valid(self):
        if self.hour > 12 and self.hour < 0:
            return False
        if self.minute > 60 and self.minute < 0:
            return False
        return True

    # porównywanie czasów
    def __lt__(self, another_time):
        if self.hour is not another_time.hour:
            return self.hour < another_time.hour
        else:
            return self.minute < another_time.minute

    # wyświetlanie
    def __str__(self):
        if self.minute < 10:
            return f'{self.hour}:0{self.minute}'
        else:
            return f'{self.hour}:{self.minute}'

    # wyświetlanie wewnątrz listy
    def __repr__(self):
        return str(self)

    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute


# tworzenie obiektów, wywoływanie metod
godzina1 = Time(11, 56)
godzina2 = Time(10, 16)
godzina3 = Time(9, 15)

if godzina1.is_valid() and godzina2.is_valid() and godzina3.is_valid():
    print("TIMES ARE VALID")

print(godzina1)
print(godzina2)
print(godzina3)

godzina4 = Time.add_two_times(godzina1, godzina2)
godzina5 = Time.add_two_times(godzina2, godzina3)
godzina6 = Time.add_two_times(godzina1, godzina3)

print(godzina4)
print(godzina5)
print(godzina6)

time_list = [godzina1, godzina2, godzina3, godzina4, godzina5, godzina6]
print(time_list)
time_list.sort()
print(time_list)


# Zadanie 7
class Samochod:
    marka = ""
    model = ""
    rok_produkcji = ""
    przebieg = ""

    def __str__(self):
        return f'To jest samochód marki {self.marka}, model {self.model}, wyprodukowany w {self.rok_produkcji} roku o przebiegu {self.przebieg}'

    def __repr__(self):
        return str(self)

    def __lt__(self, another_car):
        return self.przebieg < another_car.przebieg

    def __init__(self, marka: str, model: str, rok_produkcji: int, przebieg: int):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg


car1 = Samochod("Hyundai", "i30", 2012, 168700)
car2 = Samochod("Toyota", "Auris", 2016, 125000)
car3 = Samochod("Ford", "Focus", 2016, 83000)

lista_aut = [car2, car1, car3]
print(lista_aut)
lista_aut.sort()
print(lista_aut)
