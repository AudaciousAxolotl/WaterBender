import pygame
import math
import vectormath

class Water:
    def __init__(self,level,leak_rate,density,resistance):
        self.level=level
        self.leak_rate=leak_rate
        self.density=density
        self.resistance=resistance
