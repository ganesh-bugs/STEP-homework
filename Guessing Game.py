from random import randint
original = randint(1,100)
n=1
userinput = int(input('Enter your guess:'))

#first time check if the guess is correct
if userinput == original:
    print('You guessed the number in the first attempt')
elif (userinput < 1 or userinput >100):
    fdifference = abs(original - userinput)
    print('Your input is out of bounds. Please enter a number between 1 and 100')
else:
    #if first guess is not correct, find the difference and print warm or cold
    fdifference = abs(original - userinput)
    if fdifference<=10:
        print('WARM!')
    else:
        print('COLD!')

#from second guess onwards, print warmer or colder until the correct number is guessed
while userinput != original:
    userinput = int(input('Enter your guess:'))
    n=n+1
    if userinput <1 or userinput >100:
        fdifference = abs(original - userinput)
        print('Your input is out of bounds. Please enter a number between 1 and 100')
        continue
    newdifference = abs(original - userinput)
    if userinput == original:
        print(f'Congratulations! You guessed the correct number {original} in {n} attempts')
    elif newdifference < fdifference:
        print('WARMER!')
    else:
        print("COLDER!")
    fdifference=newdifference