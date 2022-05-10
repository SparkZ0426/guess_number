while True:
    try:
        guess_number = getInputFromUser()
    except ValueError:
        print("You have entered the wrong format, you should enter 13 instead of thirteen")
    else:
        print("You have entered the correct format for numbers")