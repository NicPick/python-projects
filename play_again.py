def play_again():
    while True:
        again = input("Play again (y/n): ")
        if again == "y":
            pass  ##play()
        elif again == "n":
            print("Thank you for playing, Bye!")
            break
        else:
            print("Please enter y OR n")
            continue
