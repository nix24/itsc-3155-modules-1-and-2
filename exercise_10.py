#Created by Jaylon Carrington

string = input("Enter a string: ")

#convert the str to a list
list_string = list(string)
print(list_string)

list_string_split = []

for i in range(0, len(list_string), 3):
    list_string_split.append(list_string[i:i+3])
print(list_string_split)