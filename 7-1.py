from math import pi


class circle:
    Pi = pi
    r = 0

    def __init__(self, r):
        self.r = r

    def __del__(self):
        print("Object is deleted")

    def area(self):
        return self.Pi * (self.r**2)

    def prime(self):
        return 2 * self.Pi * self.r

    def __str__(self):
        s = "R: " + str(self.r)
        s += "\t\tArea: " + str(self.area())
        s += "\t\tprime: " + str(self.prime())
        return s


r = int(input("Enter r: "))
c = circle(0)
print(str(c))
c = circle(r)
print(str(c))
del c
