import math
def area(base,height):
    '''
    (number,number)->number
    return the area of a triangle with given base and height
    >>>area(3,4)
    6
    '''
    return base * height / 2


def perimeter(side1,side2,side3):
    '''
    (number,number,number)->number
    return the perimeter of a triangle with given the length of the sides
    >>>perimeter(3,4,5)
    6
    '''
    return side1+side2+side3

def semiperimeter(side1,side2,side3):
    return perimeter(side1,side2,side3)/2


def area_hero(side1,side2,side3):
    semi=semiperimeter(side1,side2,side3)
    area=math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
    return area
