counter = 5
number = 76
while counter > 0:
    guess = int(input('Enter a number between 1 - 100: '))
    if guess > number:
        msg = "you are too high"
    elif guess < number:
        msg = "you are too low"
    else:
        msg = "Congrats"
    print(msg)
    if msg == "Congrats":
        counter = 0
    else:
        counter -= 1