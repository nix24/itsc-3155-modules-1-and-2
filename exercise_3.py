#Done by Jaylon Carrington
#create number var. If num is not greater than 1
#tell them to input again. repeat until num is greater than 1

isGreaterThanOne = False
while isGreaterThanOne == False:
    num = int(input("Enter a number greater than 1: "))
    if num > 1:
        isGreaterThanOne = True
    else:
        print("Please enter a number greater than 1")

for i in range(num + 1):
    square_num = i**2
    print(f"the square of {i} is {square_num}")
    