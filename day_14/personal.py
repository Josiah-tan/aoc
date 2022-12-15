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
        return hash(self.x ^ self.y)

    def __rmul__(self, obj):
        return self.__mul__(obj)

    def __mul__(self, obj):
        if type(obj) == int:
            return Point(self.x * obj, self.y * obj)
        else:
            return NotImplementedError


def sign(x):
    return (x > 0) - (x < 0)
