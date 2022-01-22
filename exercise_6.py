#Created by Jaylon Carrignton
checker = False
while checker == False:
    row_input = int(input("Enter a row from 1-5: "))
    column_input = int(input("Enter a column from 1-5: "))
    
    #if either row or column input is not betweeen 1-5, ask for input again
    if row_input < 1 or row_input > 5 or column_input < 1 or column_input > 5:
        print("Invalid input. Please try again.")
        checker = False
    else:
        checker = True    
    
for i in range(5):
    for j in range(5):
        if i == (row_input)-1 and j == (column_input)-1:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()