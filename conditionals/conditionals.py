password = input("Enter your password: ")

if len(password) < 10:
    print('Password invalid')
elif " " in password:
    print('Password invalid')
else:
    print('Valid password')

