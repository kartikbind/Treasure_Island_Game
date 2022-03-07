print("Welcome to Treasure Island\nYour mission is to find the treasure.\n")
choice = str(input("You're at a cross road. where do you want to go? Type 'left' or 'right'"))
if choice == 'left':
    choice = str(input("You come to a lake. There is an island int he middle of the lake."
                       "type 'wait' to wait for a boat. Type 'swim to swim across."))
    if choice == 'wait':
        choice = str(input("You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and"
                           "one blue. Which colour do you choose?"))
        if choice == 'yellow':
            print("You Win!")
        else:
            print("Game Over!")
            exit(0)
    else:
        print("Game Over!")
        exit(0)
else:
    print("Game Over!")
    exit(0)
