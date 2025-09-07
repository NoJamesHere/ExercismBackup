def triangle(sides):
    a, b, c = sorted(sides)  
    return a > 0 and a + b > c

def equilateral(sides):
    if triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if triangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
        return sides[0] == sides[1] != sides[2] or sides[0] == sides[2] != sides[1] or sides[1] == sides[2] != sides[0]
    return False


def scalene(sides):
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[2] != sides[1] and triangle(sides)
