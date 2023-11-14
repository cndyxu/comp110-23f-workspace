"""Challenge Question Class."""
from __future__ import annotations
 
 
class Point:
    """Class to represent (x,y) coordinate point."""
    
    x: float
    y: float
    
    def __init__(self, x=0.0, y=0.0):
        """Default point parameters."""
        self.x = x
        self.y = y

    def scale_by(self, factor: int) -> None:
        """Modify (or mutate) a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Make a new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __mul__(self, factor: int | float) -> Point:
        """Returns a new point where x and y are multiplied by a factor."""
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)
        
    def __add__(self, operand: int | float) -> Point:
        """Returns a new point that has been added from x and y."""
        new_x = self.x + operand
        new_y = self.y + operand
        return Point(new_x, new_y)
        
    def __str__(self):
        """Returns points in a readable way."""
        return f"x: {self.x}; y: {self.y}"
