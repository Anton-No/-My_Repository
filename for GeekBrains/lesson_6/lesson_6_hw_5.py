#5. Реализовать класс Stationery (канцелярская принадлежность).

#    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.



class Stationery:
    def __init__(self, title="drawing"):
        self.title = title
        
    def draw(self):
        print(f"start drawing {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"drawing with {self.title} pen")


class Pencil(Stationery):
    def draw(self):
        print(f"drawing with {self.title} pencile")


class Marker(Stationery):
    def draw(self):
        print(f"drawing with {self.title} marker")


stat = Stationery()
stat.draw()

pen = Pen("Pen_1")
pen.draw()

pencil = Pencil("Pencil_1")
pencil.draw()

marker = Marker("Marker_1")
marker.draw()