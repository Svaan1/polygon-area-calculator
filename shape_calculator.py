
from math import floor


class Rectangle:

    def __init__(self,width,heigth):
        self.width = width
        self.height = heigth

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height
    
    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2)**.5
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            lines = str()
            for c in range(self.height):
                lines += '*' * (self.width) + '\n'
        return lines
    
    def get_amount_inside(self,shape):
        height_times = floor((self.height/shape.height))
        width_times = floor((self.width/shape.width))
        return height_times * width_times

class Square(Rectangle):

    def __init__(self,side):
        self.height = side
        self.width = side

    def __str__(self):
        return f'Square(side={self.height})'
        
    def set_side(self,side):
        self.height = side
        self.width = side
    
    def set_width(self, side):
        self.height = side
        self.width = side
    
    def set_height(self, side):
        self.height = side
        self.width = side
    


