"""
Program: NumpyCalculation class
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

import numpy as np

class MatrixOperations:
    def __init__(self, matrix, array=None):
        """
        Initializes a MatrixOperations object with a matrix and an array (optional).
        """
        self.matrix = matrix
        self.array = array
    
    def create_array(self, my_list):
        """
        Creates a NumPy array from a Python list and stores it in self.array.
        Returns the created array.
        """
        my_array = np.array(my_list)
        self.array = my_array
        return self.array
    
    def create_array_with_arange(self, start, end, step):
        """
        Creates a NumPy array using arange function with the specified start, end, and step values.
        Stores the created array in self.array and returns it.
        """
        my_array = np.arange(start, end, step)
        self.array = my_array
        return self.array
    
    def create_zeros_array(self, shape):
        """
        Creates a NumPy array of zeros with the specified shape.
        Stores the created array in self.array and returns it.
        """
        zeros_array = np.zeros(shape)
        self.array = zeros_array
        return self.array
    
    def create_ones_array(self, shape):
        """
        Creates a NumPy array of ones with the specified shape.
        Stores the created array in self.array and returns it.
        """
        ones_array = np.ones(shape)
        self.array = ones_array
        return self.array
    
    def create_identity_matrix(self, n):
        """
        Creates an identity matrix of size n x n.
        Stores the created matrix in self.matrix and returns it.
        """
        identity_matrix = np.eye(n)
        self.matrix = identity_matrix
        return self.matrix
    
    def get_matrix_element(self, row, col):
        """
        Retrieves the element at the specified row and column indices from self.matrix.
        Returns the element value.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            return self.matrix.item(row, col)
        else:
            raise ValueError("Matrix is not initialized.")
    
    def get_subarray(self, start, end):
        """
        Retrieves a subarray from self.array starting from the start index (inclusive) and ending at the end index (exclusive).
        Returns the subarray.
        Raises a ValueError if the array is not initialized.
        """
        if self.array is not None:
            return self.array[start:end]
        else:
            raise ValueError("Array is not initialized.")
    
    def get_mean(self):
        """
        Computes the mean of self.matrix.
        Returns the mean value.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            return np.mean(self.matrix)
        else:
            raise ValueError("Matrix is not initialized.")
    
    def get_median(self):
        """
        Computes the median of self.array.
        Returns the median value.
        Raises a ValueError if the array is not initialized.
        """
        if self.array is not None:
            return np.median(self.array)
        else:
            raise ValueError("Array is not initialized.")
    
    def get_correlation(self, array):
        """
        Computes the correlation coefficient between self.matrix and the specified array.
        Returns the correlation matrix.
        Raises a ValueError if the matrix or array is not initialized.
        """
        if self.matrix is not None and self.array is not None:
            corr_matrix = np.corrcoef(self.matrix, array)
            return corr_matrix
        else:
            raise ValueError("Matrix or array is not initialized.")
    
    def get_variance(self):
        """
        Computes the variance of self.matrix.
        Returns the variance value.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            return np.var(self.matrix)
        else:
            raise ValueError("Matrix is not initialized.")
    
    def get_std_deviation(self):
        """
        Computes the standard deviation of self.matrix.
        Returns the standard deviation value.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            return np.std(self.matrix)
        else:
            raise ValueError("Matrix is not initialized.")
    
    def create_random_matrix(self, n, m):
        """
        Creates a random matrix of size n x m with values ranging from 0 to 10 (exclusive).
        Stores the created matrix in self.matrix and returns it.
        """
        random_matrix = np.random.randint(0, 10, size=(n, m))
        self.matrix = random_matrix
        return self.matrix
    
    def normalize_matrix(self):
        """
        Normalizes the values of self.matrix by dividing them by the maximum absolute value.
        Returns the normalized matrix.
        Raises a ValueError if the matrix is notinitialized.
        """
        if self.matrix is not None:
            max_abs_value = np.max(np.abs(self.matrix))
            self.matrix = self.matrix / max_abs_value
            return self.matrix
        else:
            raise ValueError("Matrix is not initialized.")
    
    def divide_by_max_element(self):
        """
        Divides the values of self.matrix by the maximum absolute value.
        Returns the modified matrix.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            max_abs_value = np.max(np.abs(self.matrix))
            self.matrix = self.matrix / max_abs_value
            return self.matrix
        else:
            raise ValueError("Matrix is not initialized.")
    
    def compute_variance(self):
        """
        Computes the variance of self.matrix and rounds it to 2 decimal places.
        Returns the rounded variance value.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            variance = np.var(self.matrix)
            return round(variance, 2)
        else:
            raise ValueError("Matrix is not initialized.")
    
    def compute_variance_formula(self):
        """
        Computes the variance of self.matrix using the formula and rounds it to 2 decimal places.
        Returns the rounded variance value.
        Raises a ValueError if the matrix is not initialized.
        """
        if self.matrix is not None:
            mean = np.mean(self.matrix)
            deviations = self.matrix - mean
            squared_deviations = deviations ** 2
            variance = np.mean(squared_deviations)
            return round(variance, 2)
        else:
            raise ValueError("Matrix is not initialized.")