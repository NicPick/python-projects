import random

words = [
    "Bear",  # 4 letters
    "Wolf",
    "Deer",
    "Frog",
    "Crab",
    "Duck",
    "Lion",
    "Toad",
    "Elephant",  # 5 letters
    "Giraffe",
    "Monkey",
    "Tiger",
    "Rabbit",
    "Parrot",
    "Snake",
    "Horse",
    "Dolphin",
    "Jaguar",
    "Donkey",  # 6 letters
    "Falcon",
    "Turtle",
    "Penguin",
    "Leopard",
    "Gorilla",
    "Hamster",
    "Lobster",
    "Flamingo",
    "Scorpion",
    "Squirrel",
]

# Visual stages
stages = [
    """
    -----
    |    |
    |    O
    |   /|\\
    |   / \ 
    |
    """,
    """
    -----
    |    |
    |    O
    |   /|\\
    |   
    |
    """,
    """
    -----
    |    |
    |    O
    |    |
    |   
    |
    """,
    """
    -----
    |    |
    |    
    |    O
    |   /|\\
    |   / \\
    """,
    """
    -----
    |
    |    
    |    O/
    |   /|
    |   / \\
    """,
    """
    |    
    |    
    |    O/
    |   /|
    |   / \\
    """,
    """
     O/
    /|
    / \\
    """,
]

you_win = [
    """
   \\|//

    \O/
     |
    / \\
    """,
]


##--------------------------------------------------------------------


## All game logic
def play():
    ## Game starts
    print("-------------------------------------------------------")
    print("Welcome to Hangman game!")
    print("Category: Animal")
    print()

    lives = 6
    guessed_letters = []  # List for collecting already guessed letters
    secret_word = random.choice(words).lower()  # Random word from the list

    print()
    # for letter in secret_word:
    # print("_", end=" ")

    while True:

        # Ask for input
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
        guess = input("Guess a letter in the secret word: ")
        guess = guess.lower()
        print()

        # Guess needs to be alphabet only
        if guess.isalpha():
            # Check if player has already guess that alphabet,
            # If not then add it to the already guessed list
            # If not then the game goes further
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                # Loop through the "secret word" one alphabat after one
                # If that alphabet also in the guessed list
                # Then print the alphabet
                # Otherwise print _
                if guess not in secret_word:
                    lives = lives - 1
                    if lives > 0:
                        print()
                        print(
                            f"Letter {guess} doesn't exist in the secret word. You have {lives} lives left"
                        )
                    elif lives == 0:
                        print(stages[lives])
                        print()
                        print("Game over! NO lives left...")
                        print(f"The secret word is: {secret_word.upper()}")
                        print()
                        break

                elif all(letter in guessed_letters for letter in secret_word):
                    print()
                    print(you_win[0])
                    print(
                        f"Good Job! You have the secret word: {secret_word.upper()} !!!"
                    )
                    print()
                    break
                elif guess in secret_word:
                    print()
                    print(f"Nice guessed! You still have {lives} lives left")
            else:
                print("You've already guessed this letter. Try another one.")

        else:
            print("Please enter a letter only!")

        print(stages[lives])
        print(f"Guessed: {guessed_letters}")
        print("----------------------------------------------------------------")
        print()
        print()


def play_again():
    while True:
        again = input("Play again (y/n): ")
        print()
        if again == "y":
            play()
        elif again == "n":
            print("Thank you for playing, Bye!")
            break
        else:
            print("Please enter y OR n")
            continue


def main():

    play()
    play_again()


main()
