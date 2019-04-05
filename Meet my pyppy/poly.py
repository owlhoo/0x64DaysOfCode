class Shape:

    def calculate_area(self):
        raise NotImplemented


class Square(Shape):
    side_len = 2

    def calculate_area(self):
        return self.side_len * 2


class Triangle(Shape):
    base_len = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_len * self.height


def get_area(input_object):
    print(input_object.calculate_area())


shape = Shape()
square = Square()
triangle = Triangle()

get_area(square)
get_area(triangle)
get_area(shape)

