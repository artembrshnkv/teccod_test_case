from math import sqrt


class Point:
    def __init__(self, x: int | float, y: int | float):
        self.__x = x
        self.__y = y

    @staticmethod
    def find_distance(point_a, point_b):
        xa = point_a.x_coordinate
        xb = point_a.y_coordinate
        ya = point_b.x_coordinate
        yb = point_b.y_coordinate

        return sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

    @property
    def x_coordinate(self) -> int | float:
        return self.__x

    @x_coordinate.setter
    def x_coordinate(self, new_x: int | float):
        self.__x = new_x

    @property
    def y_coordinate(self) -> int | float:
        return self.__y

    @y_coordinate.setter
    def y_coordinate(self, new_y: int | float):
        self.__y = new_y


if __name__ == '__main__':
    pa = Point(x=1, y=1)
    pb = Point(x=1, y=5)

    print(Point.find_distance(pa, pb))
