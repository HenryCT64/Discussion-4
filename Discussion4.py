import math

class Rectangle():
    # Create the constructor "__init__" method
    def __init__(self,width,height):
    # YOUR CODE HERE
        self.width = width
        self.height = height


    # Create the "__str__" method
    def __str__(self):
    # YOUR CODE HERE
        return f"A rectangle with width {self.width} and height {self.height}"


    # Create the "area_calculator" method
    def area_calculator(self):
    # YOUR CODE HERE
        return (self.width * self.height)

    def __eq__(self, other):
        return ((self.height == other.height) and (self.width == other.width))


    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE


    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()
