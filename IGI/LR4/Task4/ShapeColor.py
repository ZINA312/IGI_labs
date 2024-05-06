"""
Program: ShapeColor class
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

class ShapeColor:
    def __init__(self, color):
        """
        Initializes a ShapeColor object with the specified color.
        """
        self._color = color

    @property
    def color(self):
        """
        Getter method for the color attribute.
        Returns the current color of the shape.
        """
        return self._color

    @color.setter
    def color(self, value):
        """
        Setter method for the color attribute.
        Sets the color of the shape to the specified value.
        """
        self._color = value