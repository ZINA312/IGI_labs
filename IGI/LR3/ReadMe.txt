----main.py ----
main() - starts the program, provides a menu, and is responsible for starting the rest of the tasks
Args:
None
Returns:
None

----Task1.py ----
RunTask1() - Performs Task 1: Calculate ln(x+1) and output the results. Asks the user for the value of 'x' and the desired precision of 'eps' to calculate the natural logarithm (x+1). It then calls the NaturalLog function to perform calculations and outputs the results.

Args:
None
Returns:
None

NaturalLog() - Calculates the natural logarithm (x+1).
Calculates the natural logarithm (x+1) with a given precision of 'eps'. It uses the Taylor series to approximate the value of the logarithm.

Args:
x (float): The value of 'x' to calculate the natural logarithm for.
eps (float): The required accuracy for calculation.
Returns:
dict: A dictionary with the results of calculations, including the following keys:
- 'x': The value of 'x' passed to the function.
- 'n': The number of iterations performed to achieve the specified accuracy.
- 'F(x)': Approximate value of the natural logarithm (x+1).
- 'Math F(x)': The exact value of the natural logarithm (x+1) calculated using the math.log(1 + x) function.
- 'eps': The specified accuracy of 'eps'.


----Task2.py----

RunTask2() - Starts Task 2: counting the number of natural numbers in the list.
Organizes a loop that accepts integers from the user or generates a sequence of numbers. Then it counts the number of natural numbers in the list and outputs the results.

Args:
None
Returns:
None

@CheckIntList
CountNaturalNum(list) - Counts the number of natural numbers in the list.
Accepts a list of integers and counts the number of natural numbers in the list. She uses the `CheckIntList` decorator to check that the list contains only integers.

Args:
lst (list): A list of integers.
Returns:
int: The number of natural numbers in the list.

CheckNaturalNum() - Checks whether the number is natural.
Accepts an integer and checks whether it is natural (greater than zero).

Args:
num (int): An integer to check.
Returns:
int: 1 if the number is natural, otherwise 0.

----Task3.py----

RunTask3() - Starts Task 3: checking whether the entered string is an octal number.
Prompts the user to enter a string and checks whether the entered string is an octal number. Then it outputs the corresponding result.

Args:
None
Returns:
None

IsOctalNum(str) - Checks whether the string is an octal number.
Accepts a string and checks if it is an octal number. It tries to convert the string to a base 8 number and then compares the result with the original string. If the result of the conversion of the original string matches the original string, then True is returned, otherwise False is returned.

Args:
string (str): The input string to check.
Returns:
bool: True if the string is an octal number, otherwise False.

----Task4.py----

RunTask4() - Starts Task 4: String processing.
Prompts the user to choose to enter a string (manually or using the default string) and performs three subtasks:
- a) determining the number of words in a line and displaying all words with an odd number of letters on the screen;
- b) search for the shortest word that starts with the letter "i";
- c) output of repeated words.

Args:
None
Returns:
None

CountOddLengthWords(str) - Determines the number of words in a string and displays all words with an odd number of letters.

Args:
string (str): Input string.
Returns:
None

FindShortestWordStartsWithI(str) - Finds the shortest word that starts with the letter "i" in the string and displays it on the screen.

Args:
string (str): Input string.
Returns:
None

FindDuplicateWords(str) - Displays repeated words in a line.

Args:
string (str): Input string.
Returns:
None

----Task5.py----

RunTask5() - Starts Task 5: List processing.
Prompts the user to choose to enter a list (manually or generate a list) and performs two subtasks:
- Find the sum of the list items with odd numbers.
- Find the sum of the list items located between the first and last negative elements.

Args:
None
Returns:
None

SumOfOddElements(list) - Calculates the sum of the list items with odd numbers.

Args:
lst (list): The input list.
Returns:
float: The sum of the elements with odd numbers.

SumOfElemsBetweenNegatives(list) - Calculates the sum of the list items located between the first and last negative elements.

Args:
lst (list): The input list.
Returns:
float: The sum of the elements between the first and last negative elements.

----Generators.py----

GenerateIntList(int, int, int) - Generates an integer.

Args:
fromNum (int): The initial value of the range (inclusive).
toNum (int): The final value of the range (inclusive).
count (int): The number of items in the list.
Returns:
int: A random integer.

GenerateFloatList(int, int, int) - Generates a real number.

Args:
fromNum (float): The initial value of the range (inclusive).
toNum (float): The final value of the range (inclusive).
count (int): The number of items in the list.
Returns:
float: A random real number.

----Checkers.py----

CheckFloatNum(str) - Checks whether the input value is a real number.

Args:
num (str): Input value.
Returns:
bool: True if the input value is a real number, otherwise False.

CheckIntNum(str) - Checks whether the input value is an integer.

Args:
num (str): Input value.
Returns:
bool: True if the input value is an integer, otherwise False.

----InputFuncs.py----

XInputTask1() is a function for entering the value of x for task 1.
Requests the value of x, checks it, and returns it for task 1.

Args:
None
Returns:
float: The entered value of x.

EPSInputTask1() is a function for entering the eps value for task 1.
Requests the eps value, checks it, and returns it for task 1.

Args:
None
Returns:
float: The entered eps value.

ManualInputTask2() is a function for manually entering a list of integers for task 2.

Requests integers and checks them. When you enter 0, it completes the loop and returns a list of numbers.

Args:
None
Returns:
list: A list of integers.

GenerativeInputTask2() is a function for generating a random list of integers for task 2.

Uses the generator from the module "Generators.py ".

Args:
None
Returns:
list: A list of integers.

StringInputTask3() is a function for entering a string for task 3.

Requests a string to be entered.

Args:
None
Returns:
str: The entered string.

ManualInputTask4() is a function for entering a line for task 4.

Requests a string to be entered.

Args:
None
Returns:
str: The entered string.

DefaultInputTask4() is a function to get the default string value for task 4.

Returns the default string from the module "Data.py "

Args:
None
Returns:
str: The default string value.

LengthInputTask5() is a function for entering the number of list items for task 5.

Requests an integer and checks it.

Args:
None
Returns:
int: The entered number of list items.

ListInputTask5(int) is a function for manually entering list items for task 5.

Requests real elements and verifies them.

Args:
length (int): The number of items in the list.
Returns:
list: A list of real numbers.

----Decorators.py----

The CheckIntList decorator(func) contains:
wrapper(arr) - Checks whether the function argument is a list of integers.

Args:
arr (list): A list of items.
Returns:
The result of executing the original function.
Raises:
ValueError: If the argument is not a list of integers.

----Data.py----

Contains data

task4DefaultString is the default string for task 4.