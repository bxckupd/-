from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, length):
        self.length = length
        self.name = "Shape"

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def info(self):
        print(self.name)


class Square(Shape):
    def __init__(self, side):
        super().__init__(side)
        self.side = side
        self.name = 'Квадрат'

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side

    def info(self):
        return self.name

    def __str__(self):
        return f'{self.name} со стороной {self.side} см'

    def __eq__(self, other):
        return self.side ** 2 == other.side ** 2

    def __len__(self):
        return self.side * 4


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius
        self.name = "Круг"

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def info(self):
        return self.name

    def __str__(self):
        return f'{self.name} с радиусом {self.radius} см'

    def __eq__(self, other):
        return 3.14 * self.radius ** 2 == 3.14 * other.radius ** 2

    def __len__(self):
        return int(2 * 3.14 * self.radius)


class GeometryCalculator():
    def __init__(self):
        pass

    def validate_positive(self, number):
        if number >= 0:
            return True
        else:
            return False

    def calculate_diagonal(self, length, width):
        return (length ** 2 + width ** 2) ** 0.5

    def is_larger(self, shape1, shape2):
        if shape1.calculate_area() > shape2.calculate_area():
            return 'shape1 is larger'
        elif shape1.calculate_area() < shape2.calculate_area():
            return 'shape2 is larger'
        else:
            return 'shape1 = shape2'


shape1 = Square(5)
print(shape1.calculate_area())
print(shape1.calculate_perimeter())
print(shape1.info())
shape2 = Circle(5)
print(shape2.calculate_area())
print(shape2.calculate_perimeter())
print(shape2.info())
calculator = GeometryCalculator()
print(calculator.validate_positive(10))
print(calculator.calculate_diagonal(3, 4))
print(calculator.is_larger(shape1, shape2))