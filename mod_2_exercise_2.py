#shifting Capital letters by Jaylon Carrington

sentence = input("Hey, got anything you want to say: ")

#we will be shifting all Capital letters the end, keeping the order
#example: Hello World --> elloorldHW

capital_letters = []
joinedSen = ""

for i in range(len(sentence)):
    if sentence[i].isupper():
        capital_letters.append(sentence[i])

for i in range(len(sentence)):
    if sentence[i].islower():
        joinedSen += sentence[i]
print(joinedSen + "".join(capital_letters))