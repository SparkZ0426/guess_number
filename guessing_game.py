import random
secret_number = random.randint(1,100)

#try to write input function which will deal with wrong inputs
#print("The secret number is " + str (guess_number))



def getInputFromUser():
    while True:
        try:
            guess_number = int(input("Input your guessing number"))
        except:
            print("You have entered the wrong format, you should enter 13 instead of thirteen")
        else:
            print("You have entered the correct format for numbers")
            break
    return guess_number

def guessing():
    secret_number = random.randint(1,100)
    guess_count = 0
    while True:
        guess_number = getInputFromUser()
        guess_count += 1
        if guess_number == secret_number:
            print("You have guessed right, the secret number is {} ".format (secret_number))
            break
        else:
            print("You have guessed wrong, you have entered {} ".format(guess_number))
        #you need to tell people whether entered number is smaller or larger than secret number
        if guess_number < secret_number:
            print("The number you entered is smaller than the secret number")
        else:
            print("the number you have entered is greater than the secret number")

    print("You have guessed {} times and secret and the secret number is {} ".format(guess_number, secret_number))

if __name__=='__main__':
    guessing()











































