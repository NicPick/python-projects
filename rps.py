import random

choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}
list_choices = list(choices.values())


def player_choose():
    while True:
        player_choice = input("Make your choice (r=Rock/p=Paper/s=Scissors): ")

        if player_choice in choices:
            print(f"You chose: {choices[player_choice]}")
        else:
            print("Invalid input, choose (r/p/s): ")
            continue
        break
    return choices[player_choice]


def compare(player_choice, computer_choice):
    result = ""
    if player_choice == computer_choice:
        result = "EQUAL"

    elif player_choice == "Paper" and computer_choice == "Rock":
        result = "YOU WIN"

    elif player_choice == "Paper" and computer_choice == "Scissors":
        result = "YOU LOOSE"

    elif player_choice == "Rock" and computer_choice == "Scissors":
        result = "YOU WIN"

    elif player_choice == "Rock" and computer_choice == "Paper":
        result = "YOU LOOSE"

    elif player_choice == "Scissors" and computer_choice == "Paper":
        result = "YOU WIN"

    elif player_choice == "Scissors" and computer_choice == "Rock":
        result = "YOU LOOSE"
    print(f"Comp: {computer_choice} vs Yours: {player_choice}")
    print(result)
    return result


def play():
    comp_score = 0
    player_score = 0

    while player_score < 3 and comp_score < 3:
        computer_choice = random.choice(list_choices)
        # print(f"Computer's choice is: {computer_choice}")

        player_choice = player_choose()
        result = compare(player_choice, computer_choice)

        if result == "YOU WIN":
            player_score = player_score + 1
        elif result == "YOU LOOSE":
            comp_score = comp_score + 1

        print(f"Your score: {player_score}")
        print(f"Computer's score: {comp_score}")

    if player_score < comp_score:
        print("You loose...")
    elif player_score > comp_score:
        print("Congratulations!!! YOU WIN!!!")


def play_again():

    while True:
        again = input("Do you want to play again? Enter y = Yes or n = No: ")
        if again == "y":
            play()
        elif again == "n":
            print("Bye!")
            break
        else:
            print("Please enter y or n: ")
            continue


def main():
    play()
    play_again()


main()
