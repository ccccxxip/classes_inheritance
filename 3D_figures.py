import math

class Format:
    def volume(self):
        raise NotImplemented("метод должег быть реализован в подклассах")

    def surface_area(self):
        raise NotImplemented("метод должег быть реализован в подклассах")

class Cube(Format):
    def __init__(self, leng):
        self.leng = leng
    def volume(self):
        return self.leng ** 3 # объем куба
    def surface_area(self):
        return 6 * (self.leng ** 2) # площадь поверхности куба

class Sphere(Format):
    def __init__(self, radius):
        self.radius = radius
    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3) # объем сферы
    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2) # площадь поверхности сферы

class Cylinder(Format):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height  # объем цилиндра
    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height) # площадь поверхности цилиндра

class Prisma(Format):
    def __init__(self, leng, width, height):
        self.leng = leng
        self.width = width
        self.height = height
    def volume(self):
        return self.leng * self.width * self.height # объем призмы
    def surface_area(self):
        return 2 * (self.leng * self.width + self.leng * self.height + self.width * self.height) # площадь поверхности призмы

class Ellipsoid(Format):
    def __init__(self, semiaxes):
        self.a, self.b, self.c = semiaxes
    def volume(self):
        return (4 / 3) * math.pi * self.a * self.b * self.c # объем эллипсоида
    def surface_area(self):
        p = 1.6075  # приближение
        return 4 * math.pi * ((self.a * self.b) ** p + (self.b * self.c) ** p + (self.a * self.c) ** p) ** (1/p) # площадь поверхности эллипсоида

def check(shapes):
    total_volume = sum(shape.volume() for shape in shapes)
    matching_shapes = [shape for shape in shapes if shape.volume() >= total_volume - shape.volume()]
    return matching_shapes



shapes_list = [
    Cube(5),
    Sphere(7),
    Cylinder(2, 5),
    Prisma(1, 2, 3),
    Ellipsoid((4, 5, 2))
]

for shape in shapes_list:
    print(f"{shape.__class__.__name__}: объем = {shape.volume()}, площадь поверхности = {shape.surface_area()}")

matching_figures = check(shapes_list)
if matching_figures:
    print("\nФигуры, объем которых равен или превышает суммарный объем остальных:")
    for figure in matching_figures:
        print(f"{figure.__class__.__name__}: объем = {figure.volume()}")
else:
    print("\nНет фигур с объемом, равным или превышающим суммарный объем остальных.")