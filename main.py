# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

           #module_5_4 Задача "История строительства":

class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break
   # методам:__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors
# метод __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"


    def __eq__(self,other):
        if  self.number_of_floors == other.number_of_floors:
            return True
        else: self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self,other):
        return self.number_of_floors < other.number_of_floors


    def __le__(self,other):
        return self.number_of_floors <= other.number_of_floors


    def __gt__(self,other):
       return self.number_of_floors > other.number_of_floors

    def __ge__(self,other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self,other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
           self.number_of_floors += value
           return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __del__(self):
       print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 30)
print(House.houses_history)
h2 = House('магазин', 4)
print(House.houses_history)
h3 = House( 'паркинг',8 )
print(House.houses_history)

# Удаление объектов
del h3
del h2
del h1
print(House.houses_history)