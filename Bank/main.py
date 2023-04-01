print('Welcome to Thembe Bank of Nkandla ATM')
restart = 'Y'
chances = 3
balance = 50.54


def instructions():
    print('Please enter 1 for your balance')
    print('Please enter 2 to make a withdrawal')
    print('Please enter 3 to deposit')
    print('Please enter 4 to return card')


while chances >= 0:
    pin = int(input('Please enter your 4 digit pin: '))
    if pin == 1234:
        print('You entered a correct pin')
        while restart not in ('n', 'N', 'no', 'No', 'NO', 'nO'):
            instructions()
            choice = int(input('What would you like to choose? '))
            if choice == 1:
                print('Your balance is, ', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'N', 'no', 'No', 'NO', 'nO'):
                    print('Thank you')
                    break
            elif choice == 2:
                withdrawal = float(input('How much you want to withdraw? '))
                if withdrawal in [10, 20, 30, 80, 100]:
                    balance -= withdrawal
                    print('Your new balance is, ', balance)
                    restart = input('Would you like to go back? ')
                    if restart in ('n', 'N', 'no', 'No', 'NO', 'nO'):
                        print('Thank you')
                        break
                elif withdrawal != [10, 20, 30, 40, 100]:
                    print('Invalid amount, retry')
                    restart = 'Y'
                elif withdrawal == 1:
                    withdrawal = float(input('Enter reasonable amount to withdraw '))

            elif choice == 3:
                deposit = float(input('Enter amount you want to deposit '))
                balance += deposit
                print('Your new balance is, ', balance)
                restart = input('Would you like to go back? ')
                if restart in ('n', 'N', 'no', 'No', 'NO', 'nO'):
                    print('Thank you')
                    break

            elif choice == 4:
                print('Your card is returned...\nThank you for your service')
                break
    else:
        print('Pin incorrect')
        chances -= 1
        if chances == 0:
            print('Your account is locked')
            break
