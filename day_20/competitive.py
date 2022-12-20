class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def int(self):
        return Point(int(self.x), int(self.y))

    def __repr__(self) -> str:
        return(f"P{self.x, self.y}")

    def __add__(self, obj):
        return Point(self.x + obj.x, self.y + obj.y)
    
    def __sub__(self, obj):
        return Point(self.x - obj.x, self.y - obj.y)
        
    def __abs__(self):
        return Point(abs(self.x), abs(self.y))
        
    def distanceManhattan(self, obj):
        distance = abs(self - obj)
        return distance.x + distance.y

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __rmul__(self, obj):
        return self.__mul__(obj)

    def __mul__(self, obj):
        if type(obj) == int:
            return Point(self.x * obj, self.y * obj)
        else:
            return NotImplementedError

class Line:
    def __init__(self, point: Point, gradient) -> None:
        self.gradient = gradient
        self.intercept = point.y - gradient * point.x
    
    def intersection(self, obj):
        if self.gradient == obj.gradient:
            raise ValueError("gradients are the same")
        else:
            x = (obj.intercept - self.intercept) / (self.gradient - obj.gradient)
            y = self.gradient * x + self.intercept
        return Point(x, y)

    def __repr__(self):
        return f"(m, y) = ({self.gradient}, {self.intercept})"
    
    def __eq__(self, obj):
        return self.gradient == obj.gradient and self.intercept == obj.intercept
    
    def __hash__(self):
        return hash((self.gradient, self.intercept))

def sign(x):
    return (x > 0) - (x < 0)

