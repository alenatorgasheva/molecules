import turtle as tr
import random


class Molecules:
    """Класс молекул"""
    lst_molecules = []
    x = property()
    y = property()

    def __init__(self, x=0.0, y=0.0, radius=1.0, color='black', speed=1):
        """Инициализация"""
        if x:
            self.__x = float(x)
        else:
            self.__x = 0.0

        if y:
            self.__y = float(y)
        else:
            self.__y = 0.0

        if radius:
            self.radius = float(radius)
        else:
            self.radius = 5.0

        if color:
            self.color = color
        else:
            self.color = 'black'

        if speed:
            self.speed = int(speed)
        else:
            self.speed = 1
        Molecules.lst_molecules.append(self)

    def __str__(self):
        """Строковое представление"""
        s = '({}, {})\n'.format(self.__x, self.__y)
        s += 'radius: {}\n'.format(self.radius)
        s += 'color: {}\n'.format(self.color)
        return s

    @x.setter
    def x(self, new_x):
        """Установка нового знчения координаты x"""
        self.__x = new_x

    @x.getter
    def x(self):
        """Получение координаты x"""
        return self.__x

    @y.setter
    def y(self, new_y):
        """Установка нового знчения координаты y"""
        self.__y = new_y

    @y.getter
    def y(self):
        """Получение координаты y"""
        return self.__y

    def show(self):
        """Метод, рисующий молекулу"""
        tr.tracer(0)
        tr.hideturtle()
        tr.penup()
        tr.goto(self.__x, self.__y)
        tr.pendown()
        tr.pencolor(self.color)
        tr.fillcolor(self.color)
        tr.begin_fill()
        tr.circle(self.radius)
        tr.end_fill()

    @classmethod
    def act(cls):
        """Движение молекул"""
        for _ in range(1000):
            tr.clear()
            for molecule in Molecules.lst_molecules:
                dx = random.randint(-1, 1)
                dy = random.randint(-1, 1)
                molecule.x = molecule.x + dx * molecule.speed
                molecule.y = molecule.y + dy * molecule.speed
                molecule.show()
            tr.update()
