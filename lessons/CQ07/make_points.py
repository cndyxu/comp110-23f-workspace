"""Testing points for Point."""
from lessons.CQ07.point import Point

p = Point(2, 4)
print(p.x)

p.scale_by(3)
print(p.x)

p2: Point = p.scale(1)
p2: Point = Point (p.x, p.y)