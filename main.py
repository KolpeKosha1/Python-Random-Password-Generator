import random
import CharLib
import time

while True:
    # Ask for user input here
    print('Welcome to Password Generator!')
    letters = int(input('How many letters you want? '))
    numbers = int(input('How many numbers you want? '))
    symbols = int(input('How many symbols you want? '))

    # Calculate the total character count
    total_characters = letters + numbers + symbols

    # time delay by 1 sec
    time.sleep(1)

    # Generate letter, symbols, and numbers here
    P = []
    for letter in range(1, letters + 1):
        a = random.choice(CharLib.Lett)
        P.append(a)
    for symbol in range(1, symbols + 1):
        s = random.choice(CharLib.Sym)
        P.append(s)
    for number in range(1, numbers + 1):
        n = random.choice(CharLib.Num)
        P.append(n)
    random.shuffle(P)
    password = ''.join(P)

    # Here the condition for password length will be checked
    while True:
        if len(password) == 8:
            print('Your password is', password)
            exit()
        elif len(password) < 8:
            print('Password should contain atleast 8 characters')
            r = input('Do you want to generate another password? (yes/no): ')
            if r.lower() == 'yes':
                break
            else:
                print('Thank you for using Password Generator')
                exit()
