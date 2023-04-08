import random, sys

print("ROCK, PAPER, SCISSORS")

wins = 0
draws = 0
losses = 0

while True:
    print("%s Wins, %s Losses, %s Draws" % (wins, losses, draws))
    while True:
        playerMove = input("Enter your move (Rock, Paper, Scissors or quit) ")
        if playerMove == "quit" or playerMove == "Quit":
            sys.exit()
        if playerMove == "Rock" or playerMove == "Paper" or playerMove == "Scissors" or playerMove == "rock" or playerMove == "scissors" or playerMove == "paper":
            break # making it possible for the player to put capital or lowercase letters
        else:
            print("You made an error while choosing, please verify your spelling.")

    
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "Rock"
    elif randomNumber == 2:
        computerMove = "Paper"
    elif randomNumber == 3:
        computerMove = "Scissors"

    print(f"{playerMove.title()} versus {computerMove.title()}")

    if playerMove == computerMove:
        print("It's a tie.")
        draws += 1
    elif playerMove == "Rock" or playerMove == "rock" and computerMove == "Scissors":
        print("You win")
        wins += 1
    elif playerMove == "Paper" or playerMove == "paper" and computerMove == "Rock":
        print("You win")
        wins += 1
    elif playerMove == "Scissors" or playerMove == "scissors" and computerMove == "Paper":
        print("You win")
        wins += 1
    elif playerMove == "Rock" or playerMove == "rock" and computerMove == "Paper":
        print("You lose")
        losses += 1
    elif playerMove == "Paper" or playerMove == "paper" and computerMove == "Scissors":
        print("You lose")
        losses += 1
    elif playerMove == "Scissors" or playerMove == "scissors" and computerMove == "Rock":
        print("You lose")
        losses += 1
    
