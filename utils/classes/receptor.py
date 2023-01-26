#!/usr/bin/env python

class Receptor:
    def __init__(self, coordinates, p0k, lk, color, radius, name):
        self.lk = lk
        self.p0k = p0k
        self.name = name
        self.color = color
        self.radius = radius
        self.coordinates = coordinates
        
    def calculate_dk(self, case):
        return 10**((self.p0k-case) / (10*self.lk))