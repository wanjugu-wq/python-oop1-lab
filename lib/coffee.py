#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = size
        self.price = price


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,value):
        if value.capitalize() in ["Small", "Medium", "Large"]:
            self.size = value
        else:
            print("size must be Small, Medium, or Large")
        
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1


