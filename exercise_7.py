#Created by Jaylon Carrington

even_num = []


while True:
    num_input = input("Enter a number: ")
    
    if num_input == "quit":
        break
    if num_input.isdigit():
        int_num = int(num_input)
        
        if int_num % 2 == 0:
            even_num.append(int_num)    

print(even_num)