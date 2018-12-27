# Example of Abstract Factory Design Pattern


class Shape:
    def __init__(self, shape=None):
        self.shape_factory = shape

    def show_perimeter_formula(self):
        shape = self.shape_factory()
        print("{} perimeter = {}".format(shape, shape.perimeter_formula()))


class Rectangle:
    def perimeter_formula(self):
        return "2 * ( a + b )"

    def __str__(self):
        return "Rectangle"


class Triangle:
    def perimeter_formula(self):
        return "a + b + c"

    def __str__(self):
        return "Triangle"


if __name__ == "__main__":

    shapes = [Shape(Rectangle), Shape(Triangle)]

    for shape in shapes:
        shape.show_perimeter_formula()
        print("My class name is : {}".format(shape.__class__.__name__))
