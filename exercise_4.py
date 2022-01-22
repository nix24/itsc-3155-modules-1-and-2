#Done by Jaylon Carrington

List_size = int(input("Enter a number: "))
num_increment = 1

my_list = []

#user will input numbers until list_size is reached 
for i in range(List_size):
    my_list.append(int(input(f"Enter Number {num_increment}: ")))
    num_increment += 1
    
print(f"List: {my_list}")

mean = sum(my_list) / len(my_list)
print(f"Average: {mean}")