import random

number = random.randint(1000, 10000)
guess = 'XXXX'
guessed = 0
count = 5
while guessed != number and count > 0:
    num = int(input('Enter a four digit number :'))
    while num not in range(1000,10000):
        print('Please enter a four digit number.')
        num = int(input('Enter a four digit number :'))
    strNum = str(num)
    strNumber = str(number)
    guessList = []
    for i in guess:
        guessList.append(i)
    j = 0
    for i in strNumber:
        if strNum[j] == i:
            guessList[j] = i
        j += 1
    guess = ''.join(guessList)
    print(guess)
    if guess.isnumeric() == True:
        guessed = int(guess)
    else:
        count -= 1
        print('remaining guesses :',count)

if count == 0:
    print('You lose. The right number was :',number)
else:
    print('You guessed correct. The number was',number)