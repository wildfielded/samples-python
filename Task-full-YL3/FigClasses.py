#!/usr/bin/python3

from math import pi as pi_


class Fig2D():
    ''' Класс двумерных фигур с общими методами всех фигур
    '''
    figure_dimension = 'Плоская фигура'

    @classmethod
    def perimeter(cls):
        return None

    @classmethod
    def square(cls):
        return None

    @staticmethod
    def image(path_to_img):
        return '/web/' + path_to_img

class Fig3D():
    ''' Класс трёхмерных фигур с общими методами всех фигур
    '''
    figure_dimension = 'Объёмная фигура'

    @classmethod
    def volume(cls):
        return None

    @staticmethod
    def image(path_to_img):
        return '/web/' + path_to_img

#####=====----- Круг и наследники -----=====#####

class Circle(Fig2D):
    figure_name = 'Круг'
    img_file = 'circle.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def perimeter(cls, r_):
        return 2 * pi_ * r_

    @classmethod
    def square(cls, r_):
        return pi_ * (r_ ** 2)


class Sphere(Circle):
    figure_name = 'Сфера'
    img_file = 'sphere.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def square(cls, r_):
        return 4 * pi_ * (r_ ** 2)

    @classmethod
    def volume(cls, r_):
        return (4 / 3) * pi_ * (r_ ** 3)


class Cylinder(Circle):
    figure_name = 'Цилиндр'
    img_file = 'cylinder.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def square(cls, r_, h_):
        return 2 * pi_ * r_ * (h_ + r_)

    @classmethod
    def volume(cls, r_, h_):
        return pi_ * (r_ ** 2) * h_


class Cone(Circle):
    figure_name = 'Конус'
    img_file = 'cone.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def square(cls, r_, h_):
        return pi_ * (r_ ** 2) + (pi_ * r_ * (r_ ** 2 + h_ ** 2) ** 0.5)

    @classmethod
    def volume(cls, r_, h_):
        return pi_ * (r_ ** 2) * h_ / 3


#####=====----- Треугольник и наследники -----=====#####

class Triangle(Fig2D):
    figure_name = 'Равнобедренный треугольник'
    img_file = 'triangle.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def perimeter(cls, a_, h_):
        return ((a_ ** 2 + h_ ** 2) ** 0.5) * 2 + a_

    @classmethod
    def square(cls, a_, h_):
        return (a_ * h_) / 2


class Pyramid3F(Triangle):
    figure_name = 'Тетраэдр'
    img_file = 'pyramid3f.jpg'

    def __init__(self):
        super().__init__()

    @classmethod
    def volume(cls, a_, h_, height_):
        return height_ * (a_ * h_) / 6


#####=====----- Квадрат и наследники -----=====#####

class Quadro(Fig2D):
    figure_name = 'Квадрат'
    img_file = 'quadro.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def perimeter(cls, a_):
        return a_ * 4

    @classmethod
    def square(cls, a_, h_):
        return a_ ** 2


class Rhombus(Quadro):
    figure_name = 'Ромб'
    img_file = 'rhombus.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def square(cls, d1_, d2_):
        return d1_ * d2_ / 2


class Cube(Quadro):
    figure_name = 'Куб'
    img_file = 'cube.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def square(cls, a_):
        return (a_ ** 2) * 6

    @classmethod
    def volume(cls, a_):
        return a_ ** 3


class Pyramid4F(Quadro):
    figure_name = 'Пирамида'
    img_file = 'pyramid4f.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def volume(cls, a_, h_):
        return (a_ ** 2) * h_ / 3


class Rectangle(Quadro):
    figure_name = 'Прямоугольник'
    img_file = 'rectangle.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def perimeter(cls, a_, h_):
        return 2 * (a_ + h_)

    @classmethod
    def square(cls, a_, h_):
        return a_ * h_


class Parallelepiped(Rectangle):
    figure_name = 'Параллелепипед'
    img_file = 'parallelepiped.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def square(cls, a_, b_, h_):
        return ((a_ * b_) + (a_ * h_) + (b_ * h_)) * 2

    @classmethod
    def volume(cls, a_, b_, h_):
        return a_ * b_ * h_


#####=====----- Трапеция и наследники -----=====#####

class Trapezoid(Fig2D):
    figure_name = 'Трапеция'
    img_file = 'trapezoid.png'

    def __init__(self):
        super().__init__()

    @classmethod
    def perimeter(cls, a_, b_, h_):
        return a_ + b_ + (((a_ - b_) ** 2) + h_ ** 2) ** 0.5

    @classmethod
    def square(cls, a_, b_, h_):
        return ((a_ + b_) * h_) / 2


#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    ttt = Sphere()
    print(ttt.figure_name)
    print(str(ttt.perimeter(3)))
    print(str(ttt.square(3)))
    print(str(ttt.volume(3)))
    print(ttt.image(ttt.img_file))

#####=====----- THE END -----=====########################################