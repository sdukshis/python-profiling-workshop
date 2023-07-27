import random

from memory_profiler import profile

class Point:
    x: float
    y: float

    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y


class Circle:
    x: float
    y: float
    radius: float

    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.radius = r

@profile
def generate_scene1() -> list[Point | Circle]:
    shapes = list()

    for _ in range(100000):
        if random.randint(0, 9) < 2:
            shapes.append(Circle(random.random(), random.random(), random.random()))
        else:
            shapes.append(Point(random.random(), random.random()))
    return shapes


# @profile
def generate_scene2() -> list[Point | Circle]:
    shapes = list()

    for _ in range(10000):
        if random.randint(0, 9) < 8:
            shapes.append(Circle(random.random(), random.random(), random.random()))
        else:
            shapes.append(Point(random.random(), random.random()))
    return shapes


if __name__ == "__main__":
    shapes1 = generate_scene1()
    shapes2 = generate_scene2()

