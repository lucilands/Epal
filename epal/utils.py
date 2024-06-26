from typing import Self

class Vector2:
    def __init__(self, x : int, y : int):
        self.x = x
        self.y = y

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)
    
    def __add__(self, other) -> Self:
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other) -> Self:
        return Vector2(self.x - other.x, self.y - other.y)
    def __mul__(self, other) -> Self:
        return Vector2(self.x * other, self.y * other)
    def __div__(self, other) -> Self:
        return Vector2(self.x / other, self.y / other)