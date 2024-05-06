"""
Program: Triangle class
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

from .GeometricShape import GeometricShape
from .ShapeColor import ShapeColor
import math
import matplotlib.pyplot as plt
import numpy as np

class PrintMixin:
    def print_info(self):
        """
        Prints information about the triangle.
        """
        print(f"Triangle: side_a={self._side_a}, side_b={self._side_b}, side_c={self._side_c}, color={self._color.color}")

class Triangle(GeometricShape, PrintMixin):
    def __init__(self, side_a, side_b, side_c, color):
        """
        Initializes a Triangle object with the specified side lengths and color.
        """
        super().__init__()
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c
        self._color = ShapeColor(color)

    def calculate_area(self):
        """
        Calculates the area of the triangle using Heron's formula.
        Returns the area of the triangle.
        """
        p = (self._side_a + self._side_b + self._side_c) / 2
        area = math.sqrt(p * (p - self._side_a) * (p - self._side_b) * (p - self._side_c))
        return area

    def get_parameters(self):
        """
        Returns a string containing the parameters of the triangle.
        """
        return f"Треугольник {self._color.color} цвета, сторона a: {self._side_a}, сторона b: {self._side_b}, сторона c: {self._side_c}"
    
    def draw(self):
        """
        Draws the triangle using matplotlib.
        Asks the user to input text for labeling the triangle.
        """
        points = np.array([[0, 0], [self._side_b, 0], [self._side_c * math.cos(self._side_a), self._side_c * math.sin(self._side_a)], [0, 0]])
        plt.plot(points[:, 0], points[:, 1], color=self._color.color)
        plt.fill(points[:, 0], points[:, 1], color=self._color.color, alpha=0.3)
        plt.axis('equal')
        
        text = input("Введите текст для подписи треугольника: ")
        
        plt.text(points[0, 0], points[0, 1], text, ha='center', va='bottom')
        
        plt.title(f"Треугольник {self._color.color} цвета, сторона a: {self._side_a}, сторона b: {self._side_b}, сторона c: {self._side_c}")
        plt.show()

    def draw_to_file(self, filename):
        """
        Draws the triangle and saves it to a file with the specified filename.
        """
        points = np.array([[0, 0], [self._side_b, 0], [self._side_c * np.cos(self._side_a), self._side_c * np.sin(self._side_a)], [0, 0]])

        plt.plot(points[:, 0], points[:, 1], color=self._color.color)
        plt.fill(points[:, 0], points[:, 1], color=self._color.color, alpha=0.3)
        plt.axis('equal')
        plt.title(f"Треугольник {self._color.color} цвета, сторона a: {self._side_a}, сторона b: {self._side_b}, сторона c: {self._side_c}")
        plt.savefig(filename)
        plt.close()