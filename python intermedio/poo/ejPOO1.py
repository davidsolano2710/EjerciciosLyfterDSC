class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

radius = float(input("Enter the radius of the circle: "))

circle1 = Circle(radius)

print(f"Area of circle with radius {circle1.radius}: {circle1.get_area()}")