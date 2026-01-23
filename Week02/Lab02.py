import random
choices = ["Rock","Paper", "Scissors"]

playChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors):")
PlayerChoice = int(playChoice)

 if playerChoice < 1 or playerChoice > 3:
    print("Error: The input should be an integer between 1 and 3!")
 else:
    #Determine the winner logic using if/elif/else
    computerChoice = random.randit(1,3)


if playerChoice == computerChoice:
print("It's a tie!")
elif (playChoice == 1 and computerChoice == 3):
    print("Rock Beats Scissors - You Win!")
elif (playChoice == 2 and computerChoice == 1):
    print("Paper beats rock. You Win!")
elif (playChoice == 3 and computerChoice == 2):
    print("Scissors beats paper. You Win!")
else:
    print("computer Wins!")