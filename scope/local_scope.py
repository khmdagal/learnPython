# Local scope
# Local scope variable is opposite of the global scope
# when we define a variable inside our function we can only
# access that variable inside the function but not outside it.

def cube(num):
    answer = num  ** 3
    print(answer)

cube(3)

def zoo():
    animal = 'Harlequin Shrimp'
    print('inside Zoo function', animal)