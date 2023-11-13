"""CQ07- Intro to OOP."""
from __future__ import annotations
__author__ = "730479883"

class Point:
    def __init__(self, x_init: float, y_init: float):
        self.x: float = x_init
        self.y: float = y_init
    
    
    def scale_by(self, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor
    

    def scale(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)