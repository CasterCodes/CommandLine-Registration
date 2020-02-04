
import time
from user import User
user = User()


def registerUser():
    while True:
        firstName = input('\n Enter first name : ')
        if firstName == '':
            print('\n First Name cant be empty')
            continue
        else:
            break
    while True:
        lastName = input('\n Enter last name : ')
        if lastName == '':
            print('\n Last name cant be empty')
            continue
        else:
            break
    while True:
        email = input('\n Enter your email : ')
        if email == '':
            print('\n Email cant be empty ')
            continue
        else:
            break
    while True:
        password = input('\n Enter your password : ')
        if password == '':
            print(' \n Password cant be empty')
            continue
        else:
            break
    while True:
        cpassword = input('\n Confirm  your password : ')
        if cpassword == '':
            print('\n Confirm password cant be empty')
            continue
        else:
            break
    while True:
        if password != cpassword:
            print('\n Passwords do not match')
            continue
        else:
            break
    if user.selectUser([email]):
        print('\n Email already available ')
        time.sleep(2)
        print('\n Please try creating an account again ')
        registerUser()
    else:
        if user.inserUserData([firstName, lastName, email, password]):
            print('\n Sign up......')
            time.sleep(2)
            print('\n Your account was successfully created')
            print("\n Please login")
            login()
        else:
            print('\n Something went wrong, Please try again')
            time.sleep(2)
            init()


def login():
    while True:
        print('\n Enter your details to login')
        Username = input('\n Enter your email: ')
        if Username == '':
            print('\n Email cant be empty')
            continue
        else:
            break
    while True:
        password = input(' \n Enter your password : ')
        if password == '':
            print('\n Password Cant be empty ')
            continue
        else:
            break
    if user.selectUser([Username]):
        current = user.selectUser([Username])
        if password != current[4]:
            print('\n Incorrect Password')
            login()
        else:
            currentUsername = f'{current[1]} {current[2]}'
            session(currentUsername)
    else:
        print(' \n User not found, please check your email or password')
        init()


def session(Username):
    print("\n "f'Welcome to your account {Username}')
    print('\n Your options: viewmembers || logout  || exit')
    option = input(' \n Enter your Option : ')
    if option == 'viewmembers':
        print('\n Users')
        print('*' * 10)
        time.sleep(5)
        for euser in user.selectUsers():
            print('\n 'f'{euser[0]} {euser[1]}')
        continuedSession(Username)
    elif option == 'logout':
        print(' \n logging out....')
        time.sleep(4)
        print(' \n logged out')
        time.sleep(2)
        login()
    elif option == 'exit':
        print('')

    else:
        print('Wrong Option')


def continuedSession(Username):
    print('\n Your options again : viewmembers || logout || exit ')
    option = input(' \n Enter your Option : ')
    if option == 'viewmembers':
        print('\n Users')
        print('*' * 10)
        time.sleep(5)
        for euser in user.selectUsers():
            print('\n 'f'{euser[0]} {euser[1]}')
        session(Username)
    elif option == 'logout':
        print(' \n logging out....')
        time.sleep(4)
        print(' \n logged out')
        time.sleep(4)
        login()
    elif option == 'exit':
        print('')

    else:
        print('Wrong Option')


def main():
    choice = input('\n Please choose your choice : ')
    if choice == 'register':
        registerUser()
    elif choice == 'login':
        login()
    else:
        print('\n Wrong choice')
        time.sleep(4)
        init()


def init():
    print("\n")
    print("#" * 20)
    print("\n")
    print("\n :: Welcome, Please follow these Instructions ::")
    print("\n")
    print("#" * 20)
    print("\n")
    print("\n  Yours choices are-> register || login ")
    time.sleep(2)
    main()


init()
