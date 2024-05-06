"""
Program: GeometricShape class
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

from abc import ABC, abstractmethod

class GeometricShape(ABC):
    @abstractmethod
    def calculate_area(self):
        """
        Abstract method to calculate the area of a geometric shape.
        Subclasses must implement this method.
        """
        pass