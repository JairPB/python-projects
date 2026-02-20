import random

user_score = 0
computer_score = 0
game = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Type rock, paper, scissors, or type q to exit: ").lower()
    computer_choice = random.choice(game)

    if user_choice == 'q':
        break

    if user_choice not in game:
        print("That doesn't exist! Try again.")
        continue
    else:
        print(f"computer chose {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print("You won a point!")
            user_score += 1
        elif user_choice == 'paper' and computer_choice == 'rock':
            print("You won a point!")
            user_score += 1
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print("You won a point!")
            user_score += 1
        else:
            print("Computer won a point!")
            computer_score += 1

if user_score > computer_score:
    print("You win!")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
elif user_score < computer_score:
    print("You lose!")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
elif (user_score and computer_score) == 0:
    print("You didn't want to play. So sad!")
else:
    print("It's a tie!")
