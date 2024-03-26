"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

Requests a string and determines the number of words in which the number of letters is odd, the shortest word for the letter i, repeated words
"""

from InputFuncs import DefaultInputTask4, ManualInputTask4

def RunTask4() -> None:
    string = str()
    print('------------------------------')
    print('а) определить количество слов в строке и вывести на экран все слова, количество букв у которых нечетное;')
    print('б) найти самое короткое слово, которое начинается на букву "i";')
    print('в) вывести повторяющиеся слова')
    print('------------------------------')
    while True:
        menu = input("1. Ввод вручную\n2. Использовать строку по умолчанию\nВвод: ")
        match menu:
            case '1':
                string = ManualInputTask4()
                break
            case '2':
                string = DefaultInputTask4()
                break
            case _:
                print('Нет такого варианта!')
                continue
    CountOddLengthWords(string)
    FindShortestWordStartsWithI(string)
    FindDuplicateWords(string)

def CountOddLengthWords(string) -> None:
    words = string.split()
    oddLengthWords = []
    for word in words:
        if len(word) % 2 != 0:
            oddLengthWords.append(word)
    print(f'Количество слов в строке: {len(words)}')
    print(f'Слова с нечетным количеством букв: {", ".join(oddLengthWords)}')

def FindShortestWordStartsWithI(string) -> None:
    words = string.split() 
    shortestWord = None
    for word in words:
        if word.startswith('i'):
            if shortestWord is None or len(word) < len(shortestWord):
                shortestWord = word
    if shortestWord is None:
        print('Нет слов, которые начинаются на i!\n')
    else:
        print(f'Самое короткое слово на i: {shortestWord}')

def FindDuplicateWords(string) -> None:
    words = string.split()
    uniqueWords = set()
    duplicateWords = set()
    for word in words:
        if word in uniqueWords:
            duplicateWords.add(word)
        else:
            uniqueWords.add(word)
    print(f'Повторяющиеся слова: {", ".join(duplicateWords)}')