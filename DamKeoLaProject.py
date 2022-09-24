from random import randint

print("\nPlease Choose Dam Keo or La: ")
player = input("Player choose: ")
computer = randint(0,2)

if computer ==0:
    computer = "Dam"
    if computer ==1:
        computer ="Keo"
    else:
        computer ="La"


print("Computer chooses: "+ computer)

if player == computer:
    print("Draw")
else:
    if player == "Keo":
        if computer =="La":
            print("Win")
        else:
            print("Lose")

    elif player == "La":
        if computer =="Keo":
            print("Lose")
        else:
            print("Win")
            
    elif player == "Dam":
        if computer =="La":
            print("Lose")
        else:
            print("Win")
    else:
        print("Wrong Input")

        
