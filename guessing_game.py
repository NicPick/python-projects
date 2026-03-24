import random


def play():

    MIN = 1
    MAX = 20

    print(f"Im thinking of a number between {MIN} and {MAX}...")
    secret = random.randint(MIN, MAX)
    guesses = 0

    while True:
        try:
            guess = int(input("Your guess: "))
        except:
            print("Please type a number!")
            continue

        if guess < MIN or guess > MAX:
            print(f"Please enter a number between {MIN} AND {MAX}")
            continue

        guesses = guesses + 1
        if guess > secret:
            print("Too high")

        elif guess < secret:
            print("Too low")

        else:
            print("Correct!!")
            print(f"You've guessed {guesses} times ")
            break


def play_again():
    while True:
        again = input("Play again (y/n): ")
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
