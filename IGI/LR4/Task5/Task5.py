"""
Program: Task 5 
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

from .NPCalc import MatrixOperations
from Checkers import CheckFloatNum, CheckIntNum
import os

def show_menu():
    '''Displays the menu options for the Numpy program.'''
    print("===== Numpy Program =====")
    print("1. Create array")
    print("2. Create array with range")
    print("3. Create zeros array")
    print("4. Create ones array")
    print("5. Create identity matrix")
    print("6. Get element")
    print("7. Get subarray")
    print("8. Get subarray")
    print("9. Get mean")
    print("10. Get median")
    print("11. Get correlation")
    print("12. Get vatiance")
    print("13. Get std deviation")
    print("14. Create random matrix")
    print("15. Normalize matrix")
    print("16. Devide by max elem")
    print("17. Compute variance")
    print("18. Compute variance by formula")
    print("0. Exit")
    print("----------------------------------")

def Task5():
    '''Executes the main logic of the Numpy program.'''
    os.system('cls')
    matrix = None
    array = None
    matrix_operations = MatrixOperations(matrix, array)
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "0":
            print("Exiting the program...")
            return
        
        elif choice == "1":
            my_list = input("Enter the list of elements: ").split()
            my_array = matrix_operations.create_array(my_list)
            print("Array created:", my_array)
        
        elif choice == "2":
            start = input("Enter the start value: ")
            end = input("Enter the end value: ")
            step = input("Enter the step value: ")
            if CheckFloatNum(start) and CheckFloatNum(end) and CheckFloatNum(step):
                start = float(start)
                end = float(end)
                step = float(step)
                my_array = matrix_operations.create_array_with_arange(start, end, step)
                print("Array created:", my_array)
            else:
                print("Invalid input. Start, end, and step values must be real numbers.")
        
        elif choice == "3":
            shape = input("Enter the shape of zeros array (e.g., '3 4' for 3 rows and 4 columns): ")
            shape_values = shape.split()
            if all(CheckIntNum(value) for value in shape_values):
                shape = tuple(map(int, shape_values))
                zeros_array = matrix_operations.create_zeros_array(shape)
                print("Zeros array created:\n", zeros_array)
            else:
                print("Invalid input. Shape values must be integers.")
        
        elif choice == "4":
            shape = input("Enter the shape of ones array (e.g., '3 4' for 3 rows and 4 columns): ")
            shape_values = shape.split()
            if all(CheckIntNum(value) for value in shape_values):
                shape = tuple(map(int, shape_values))
                ones_array = matrix_operations.create_ones_array(shape)
                print("Ones array created:\n", ones_array)
            else:
                print("Invalid input. Shape values must be integers.")
        
        elif choice == "5":
            size = input("Enter the size of the identity matrix: ")
            if CheckIntNum(size):
                size = int(size)
                identity_matrix = matrix_operations.create_identity_matrix(size)
                print("Identity matrix created:\n", identity_matrix)
            else:
                print("Invalid input. Size must be an integer.")
        
        elif choice == "6":
            row = input("Enter the row index: ")
            col = input("Enter the column index: ")
            if CheckIntNum(row) and CheckIntNum(col):
                row = int(row)
                col = int(col)
                element = matrix_operations.get_element(row, col)
                print("Element at row", row, "and column", col, "is:", element)
            else:
                print("Invalid input. Row and column indices must be integers.")
        
        elif choice == "7":
            start_row = input("Enter the start row index: ")
            end_row = input("Enter the end row index: ")
            start_col = input("Enter the start column index: ")
            end_col = input("Enter the end column index: ")
            if CheckIntNum(start_row) and CheckIntNum(end_row) and CheckIntNum(start_col) and CheckIntNum(end_col):
                start_row = int(start_row)
                end_row = int(end_row)
                start_col = int(start_col)
                end_col = int(end_col)
                subarray = matrix_operations.get_subarray(start_row, end_row, start_col, end_col)
                print("Subarray:\n", subarray)
            else:
                print("Invalid input. Row and column indices must be integers.")
        
        elif choice == "8":
            mean = matrix_operations.get_mean()
            print("Mean:", mean)
        
        elif choice == "9":
            median = matrix_operations.get_median()
            print("Median:", median)
        
        elif choice == "10":
            my_list = input("Enter the list of elements: ").split()
            correlation = matrix_operations.get_correlation(my_list)
            print("Correlation matrix:\n", correlation)
        
        elif choice == "11":
            variance = matrix_operations.get_variance()
            print("Variance:", variance)
        
        elif choice == "12":
            standard_deviation = matrix_operations.get_standard_deviation()
            print("Standard deviation:", standard_deviation)
        
        elif choice == "13":
            shape = input("Enter the shape of the random matrix (e.g., '3 4' for 3 rows and 4 columns): ")
            shape_values = shape.split()
            if all(CheckIntNum(value) for value in shape_values):
                shape = tuple(map(int, shape_values))
                random_matrix = matrix_operations.create_random_matrix(shape)
                print("Random matrix created:\n", random_matrix)
            else:
                print("Invalid input. Shape values must be integers.")
        
        elif choice == "14":
            min_value = matrix_operations.get_min_value()
            print("Minimum value:", min_value)
        
        elif choice == "15":
            max_value = matrix_operations.get_max_value()
            print("Maximum value:", max_value)
        
        elif choice == "16":
            sorted_matrix = matrix_operations.sort_matrix()
            print("Sorted matrix:\n", sorted_matrix)
        
        elif choice == "17":
            transposed_matrix = matrix_operations.transpose_matrix()
            print("Transposed matrix:\n", transposed_matrix)
        
        elif choice == "0":
            return
        
        else:
            print("Invalid choice. Please enter a valid option.")
        
        input("Press Enter to continue...")
        os.system('cls')