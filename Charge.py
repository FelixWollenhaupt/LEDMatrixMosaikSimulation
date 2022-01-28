from enum import Enum

class Charge(int, Enum):
    UNDEFINED = -1
    MINUS = 0
    PLUS = 1