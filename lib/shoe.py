#!/usr/bin/env python3

# shoe.py

class Shoe:
    '''Class representing a shoe'''

    def __init__(self, brand, size):
        '''Initialize Shoe with brand and size'''
        self.brand = brand
        self.size = size

    def cobble(self):
        '''Simulate cobbling a shoe'''
        print("Your shoe is as good as new!")
        self.condition = "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
