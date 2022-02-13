import random

score = 0


def tryAgain():
    global score
    tryAgainTXT = input("try again?(y, n): ")
    # if they user types y the game restarts and if n or anything else it will end
    if tryAgainTXT == "y":
        guessing()
    elif tryAgainTXT == "n":
        print("game ended your score was: " + str(score))
    elif tryAgainTXT != ("y", "n"):
        print("wrong input try again!")
        tryAgain()


def guessing():
    global score
    # generates the number to actually guess
    num = random.randint(1, 10)
    # sets the guess to nothing
    guess = None
    guess_count = 0
    while guess != num:
        guess = int(input("guess a number between 1 and 10: "))
        # checks if your guess is the same as the number and if it is it prints out the things below and if its not then it will add 1 to the counter and print that it was wrong
        if guess == num:
            print("congratulations. you won!")
            print("you geussed it in " + str(guess_count) + " tries")
            # adding 10 to the score???
            score += 1
            print("current score: " + str(score))
            tryAgain()

        else:
            # checks if the guessed number is lower or higher than the generated number
            if guess < num:
                print("wrong number try a higher one!")
                guess_count += 1
            elif guess > num:
                print("wrong number try a lower one!")
                guess_count += 1


print("number guesser by DarkenMo")
# calling the game
guessing()
