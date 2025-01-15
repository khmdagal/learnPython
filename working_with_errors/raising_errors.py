def get_user_name():
    inp = input('Please enter your name: ')
    if not inp.isalpha():
        raise ValueError('Only alpha characters')
    return "Your name is " + inp

print(get_user_name())