# Write program that check the average length of a name in UK.
# The program will ask you your first name and second name and then will calculate if 
# your name is longer or shorter than the average name length in UK.

avarage_UK_name_length = 6

Your_first_name = input('Enter your name')
Your_last_name = input("Enter your last name")

full_name_length = len(Your_first_name) + len(Your_last_name)

if full_name_length > avarage_UK_name_length:
    print('Your name is longer then the avarege UK name')
elif full_name_length < avarage_UK_name_length:
    print('Your name is shorter then the avarage UK name')
else:
    print('!! Woow your name is exactly the same length as the avarage UK name !!')