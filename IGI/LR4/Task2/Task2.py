from .TextAnalizer import TextAnalyzer
import os

def show_menu():
    print("===== Text Analizer Program =====")
    print("1. Analize text")
    print("2. Get hex nums")
    print("3. Check plus sign")
    print("4. Words with 4 letters")
    print("5. Vowel consonant words")
    print("6. Sort words by len")
    print("0. Exit")
    print("----------------------------------")

def Task2():
    analizer = TextAnalyzer('input.txt', 'output.txt')
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        os.system('cls')
        if choice == "1":
            analizer.analyze_text()
            print("Text has been analized, check output file!")
        elif choice == "2":
            print("Hex nums\n"+','.join(analizer.get_hex_numbers()))
        elif choice == "3":
            if(analizer.check_plus_numbers()):
                print("There are pluses after digits")
            else:
                print("There is no pluses after digits")
        elif choice == "4":
            print(f"Words with length = 4: {analizer.count_words_length_four()}")
        elif choice == "5":
            for item in analizer.find_vowel_consonant_words():
                print(f"{item[0]} : {item[1]}")
        elif choice == "6":
            print(', '.join(analizer.sort_words_by_length()))
        elif choice == "0":
            print("Exiting the task2...")
            break
        else:
            print("Invalid choice! Please try again.")