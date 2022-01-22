#Done by Jaylon Carrington

first_word = input("Enter a String: ")
second_word = input("Enter another String: ")

if first_word.startswith(second_word) or second_word.startswith(first_word):
    print("True")
else:
    print("False")
