class Point:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def int(self):
        return Point(int(self.y), int(self.x))

    def __repr__(self) -> str:
        return(f"P{self.y, self.x}")

    def __add__(self, obj):
        return Point(self.y + obj.y, self.x + obj.x)
    
    def __sub__(self, obj):
        return Point(self.y - obj.y, self.x - obj.x)
        
    def __abs__(self):
        return Point(abs(self.y), abs(self.x))
        
    def distanceManhattan(self, obj):
        distance = abs(self - obj)
        return distance.x + distance.y

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y
    
    def __hash__(self):
        return hash((self.y, self.x))

    def __rmul__(self, obj):
        return self.__mul__(obj)

    def __mul__(self, obj):
        if type(obj) == int:
            return Point(self.y * obj, self.x * obj)
        else:
            return NotImplementedError

class Cartesian:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def int(self):
        return Cartesian(int(self.x), int(self.y))

    def __repr__(self) -> str:
        return(f"P{self.x, self.y}")

    def __add__(self, obj):
        return Cartesian(self.x + obj.x, self.y + obj.y)
    
    def __sub__(self, obj):
        return Cartesian(self.x - obj.x, self.y - obj.y)
        
    def __abs__(self):
        return Cartesian(abs(self.x), abs(self.y))
        
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
            return Cartesian(self.x * obj, self.y * obj)
        else:
            return NotImplementedError

class Line:
    def __init__(self, point: Cartesian, gradient) -> None:
        self.gradient = gradient
        self.intercept = point.y - gradient * point.x
    
    def intersection(self, obj):
        if self.gradient == obj.gradient:
            raise ValueError("gradients are the same")
        else:
            x = (obj.intercept - self.intercept) / (self.gradient - obj.gradient)
            y = self.gradient * x + self.intercept
        return Cartesian(x, y)

    def __repr__(self):
        return f"(m, y) = ({self.gradient}, {self.intercept})"
    
    def __eq__(self, obj):
        return self.gradient == obj.gradient and self.intercept == obj.intercept
    
    def __hash__(self):
        return hash((self.gradient, self.intercept))

def sign(x):
    return (x > 0) - (x < 0)

