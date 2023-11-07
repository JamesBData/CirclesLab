import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius

def main():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        circle = Circle(radius)
        print(f"Diameter: {circle.calculate_diameter()}")
        print(f"Circumference: {circle.calculate_circumference()}")
        print(f"Area: {circle.calculate_area()}")

        grow_choice = input("Do you want the circle to grow? (yes/no): ").strip().lower()
        if grow_choice == 'yes':
            circle.grow()
        else:
            print(f"Goodbye! The circle's final radius is {circle.get_radius()}.")
            break

if __name__ == "__main__":
    main()
