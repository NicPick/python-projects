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


print("Welcome to Hangman game!")
print("Category: Animal")
print()


def play():
    lives = 6
    guessed_letters = []
    secret_word = random.choice(words).lower()
    for letter in secret_word:
        print("_", end=" ")
    while True:

        print()
        guess = input("Guess a letter in the secret word: ")
        guess = guess.lower()
        print()
        if not guess.isalpha():
            print("Please enter a letter only!")
            continue

        else:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                for letter in secret_word:
                    if letter in guessed_letters:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                if guess not in secret_word:
                    lives = lives - 1
                    if lives == 0:
                        print()
                        print("NO lives left")
                        print(f"The secret word is: {secret_word}")
                        print("------------------------------------------------------")
                        break
                    print()
                    print(
                        f"Letter {guess} doesn't exist in the secret word. You have {lives} lives left"
                    )
                elif all(letter in guessed_letters for letter in secret_word):
                    print()
                    print(f"Good Job! You have the secret word: {secret_word} !!!")
                    print("------------------------------------------------------")
                    break
                else:
                    print()
                    print(f"Nice guessed! You have {lives} lives left")
                    print(f"Guessed: {guessed_letters}")
                    print(
                        "----------------------------------------------------------------"
                    )
                    continue
            else:
                print("You've already guessed this letter. Try another one.")
                print(f"Guessed: {guessed_letters}")
                print(
                    "----------------------------------------------------------------"
                )
                continue

            print(f"Guessed: {guessed_letters}")
            print("----------------------------------------------------------------")


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
