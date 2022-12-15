import re
file_number = 2
if file_number == 1:
    y = 10
else:
    y = 2000000
    
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

with open(f'{file_number}.txt') as f:
    entries = [a for a in f.read().rstrip().split('\n')]
    entries = [list(map(int, re.match("Sensor at x=([\\d-]*), y=([\\d-]*): closest beacon is at x=([\\d-]*), y=([\\d-]*)", line).groups())) for line in entries]
    entries = [(Point(line[0], line[1]), Point(line[2], line[3])) for line in entries]


impossible = set()
beacons = set()
for sensor, beacon in entries:
    if (beacon.y == y):
        beacons.add(beacon.x)
    distance = sensor.distanceManhattan(beacon)
    if abs(sensor.y - y) <= distance:
        values = 2 * distance - abs(sensor.y - y) * 2 + 1
        start = sensor.x - (distance - abs(sensor.y - y))
        for i in range(start, start + values):
            impossible.add(i)


part_1 = impossible - beacons
print(f"part_1 = {len(part_1)}")

##

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
        return hash(self.gradient ^ self.intercept)

##

positive_lines = set()
negative_lines = set()

for sensor, beacon in entries:
    distance = sensor.distanceManhattan(beacon) + 1
    left = Point(sensor.x - distance, sensor.y)
    right = Point(sensor.x + distance, sensor.y)

    positive_lines.add(Line(left, 1))
    positive_lines.add(Line(right, 1))
    negative_lines.add(Line(left, -1))
    negative_lines.add(Line(right, -1))

intersection = set()
for positive_line in positive_lines:
    for negative_line in negative_lines:
        answer = negative_line.intersection(positive_line)
        if answer.int() - answer == Point(0, 0):
            intersection.add(answer.int())
        
for sensor, beacon in entries:
    intersection = {x for x in intersection if (sensor.distanceManhattan(beacon) < sensor.distanceManhattan(x))}


if file_number == 1:
    upper = 20
else:
    upper = 4000000
maybe = {point for point in intersection if (point.x <= upper and point.x >= 0 and point.y <= upper and point.y >= 0)}
point = maybe.pop()

part_2 = point.x * 4000000 + point.y
print(f"part_2 = {part_2}")
