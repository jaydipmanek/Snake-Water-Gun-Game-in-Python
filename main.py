import random

# Game Choices: 1 for Snake, -1 for Water, 0 for Gun
'''
1 -> Snake
-1 -> Water 
0 -> Gun
'''

# Computer randomly chooses from -1 (Water), 0 (Gun), or 1 (Snake)
computer = random.choice([-1, 0, 1])

# User Input: Player enters their choice (s for Snake, w for Water, g for Gun)
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Mapping user input to corresponding game value
youDict = {"s": 1, "w": -1, "g": 0}  # s -> Snake, w -> Water, g -> Gun
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}  # Reverse map to show the result

# Check if the user input is valid
if youstr not in youDict:
    print("Invalid choice! Please choose 's' for Snake, 'w' for Water, or 'g' for Gun.")
    exit()  # Exit if the input is invalid

# Map user choice to corresponding number
you = youDict[youstr]

# Show the choices made by both the player and the computer
print(f"\nYou chose: {reverseDict[you]}")
print(f"Computer chose: {reverseDict[computer]}")

# Checking the result of the game
if computer == you:
    print("It's a draw!")  # If both choices are the same

else:
    # You Win Scenarios
    if (computer == -1 and you == 1):  # Snake drinks Water
        print("You win! Snake drinks water.")
    
    elif (computer == 1 and you == 0):  # Gun kills Snake
        print("You win! Gun kills snake.")
    
    elif (computer == 0 and you == -1):  # Water destroys Gun
        print("You win! Water destroys gun.")
    
    # You Lose Scenarios
    elif (computer == 1 and you == -1):  # Snake drinks Water
        print("You lose! Snake drinks water.")
    
    elif (computer == -1 and you == 0):  # Water destroys Gun
        print("You lose! Water destroys gun.")
    
    elif (computer == 0 and you == 1):  # Gun kills Snake
        print("You lose! Gun kills snake.")
    
    else:
        print("Something went wrong!")

# Additional feature: Ask the user if they want to play again
play_again = input("\nDo you want to play again? (y/n): ").lower()

if play_again == 'y':
    # Restart the game (or you could loop this section)
    print("\nRestarting the game...\n")
else:
    print("\nThanks for playing!")
