from math import *
class Sphere:
    def area(self,r):
        return pi*(r**2)*4
    def volume(self,r):
        return (4*pi/3)*r**3
shape1=Sphere()
r=int(input('please enter r: '))
print('the area is: ',shape1.area(r))
print('the volume is: ',shape1.volume(r))