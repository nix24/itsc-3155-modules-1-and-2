#Done by Jaylon Carrington
first_arr = []
second_arr = []
third_arr = []
num_increment = 1
print("Enter 5 numbers in the first array. ")
for i in range(5):
    first_arr.append(int(input(f"Enter Number {num_increment}: ")))
    num_increment += 1

print("Enter 5 numbers in the second array. ")
for i in range(5):
    second_arr.append(int(input(f"Enter Number {num_increment}: ")))
    num_increment += 1

#iterate through both arrays and look for common numbers
#if a common number is found but already in the third array, do nothing

for i in range(len(first_arr)):
    for j in range(len(second_arr)):
        if first_arr[i] == second_arr[j] and first_arr[i] not in third_arr:
            third_arr.append(first_arr[i])

print(f"List: {third_arr}")