# guess a number between 1 and 10
import random


def guessing():
    # generates the number to actually guess
    num = random.randint(1, 10)
    # sets the guess to nothing
    guess = None
    guess_count = 0
    while guess != num:
        guess = input("guess a number between 1 and 10: ")
        guess = int(guess)

        # checks if your guess is the same as the number and if it is it prints out the things below and if its not then it will add 1 to the counter and print that it was wrong
        if guess == num:
            print("congratulations. you won!")
            print("you geussed it in " + str(guess_count) + " tries")
            tryAgain = input("try again?(y, n): ")
            # if they user types y the game restarts and if n or anything else it will end
            if tryAgain == "y":
                guessing()
            else:
                break
        else:
            print("wrong number try again!")
            guess_count += 1


print("number guesser by DarkenMo")
# calling the game
guessing()
