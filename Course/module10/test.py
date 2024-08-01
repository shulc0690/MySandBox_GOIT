from random import randrange

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        elif index == 1:
            return self.coordinates.y
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index == 1:
            self.coordinates.y = value
        else:
            raise IndexError("Index out of range")

    def __repr__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points
        self.vectors = [Vector(Point(randrange(0, max_points), randrange(0, max_points))) for _ in range(max_vectors)]
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.max_vectors:
            raise StopIteration
        vector = self.vectors[self.current_index]
        self.current_index += 1
        return vector


class RandomVectors:
    def __init__(self, max_vectors, max_points):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


# Приклад використання
vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)
