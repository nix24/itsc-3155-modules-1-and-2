#Created by Jaylon Carrington

first_list = []
unique_list = []
num_inc = 1

for i in range(10):
    first_list.append(int(input(f"Enter number {num_inc}: ")))
    num_inc += 1

print(first_list)

for i in range(len(first_list)):
    if first_list.count(first_list[i]) == 1:
        unique_list.append(first_list[i])
    
print(unique_list)