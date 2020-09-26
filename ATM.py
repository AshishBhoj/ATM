print('Welcome to SBI India ATM')
restart = ('Y')
chances = 3
balance = 90.45

while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit Pin Number'))
    if pin == (1234):
        print('You Entered Your Pin Correctly \n')
        while restart != ['n','no','N','NO']:
            print('Please Enter Option 1 for Balance Check \n')
            print('Please Enter Option 2 to make Withdraw \n')
            print('Please Enter Option 3 to add money in account \n')
            print('Please Enter Option 4 to return back to Main Menu \n')

            option = int(input('What woulld you like to choose ? '))

            if option == 1:
                print('Your Balance is Rs ',balance)
                restart = input('Would you like to go back ')
                if restart in ['n','no','N','NO']:
                    print('Thank You')
                    break

            elif option == 2:
                option2 = ('y')
                withdraw = float(input('Enter amount you would like to withdraw ?\n Rs10,Rs20,Rs40,Rs60,Rs80,Rs100'))
                if withdraw in [10,20,40,60,80,100]:
                    balance = balance - withdraw
                    print('\nYour Balance is Rs ', balance)
                    restart = input('Would you like to go back ')
                    if restart in ['n', 'no', 'N', 'NO']:
                        print('Thank You')
                        break
                elif withdraw != [10,20,40,60,80,100]:
                    print('Invalid Option, Try Again!!')
                    restart = ('Y')
                elif withdraw == 1:
                    withdraw = float(input('Please enter a desired amount'))

            elif option == 3:
                pay_in = float(input("Enter amount you would like to pay \n"))
                balance = balance + pay_in
                print('\nYour Balance is Rs ', balance)
                restart = input('Would you like to go back ')
                if restart in ['n', 'no', 'N', 'NO']:
                    print('Thank You')
                    break

            elif option == 4:
                print('Please wait whilst your card is returned\n')
                print('Thank you for Your Service \n')
                break

            else:
                print('Enter a Invalid Option \n')
                restart = ('Y')

    elif pin != (1234):
        print('Invalid Password')
        chances = chances-1
        if chances == 0:
            print('\n No more chances left')
            break






