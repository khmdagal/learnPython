# Global scope
# when we define a variable outside our function that variable is global 
# and can be accessed everywhere in our code
animal = "lemur"

print('outside of function', animal)

def animal_function():
    print('inside of function', animal)

animal_function()



# ======= Important ========
# variables declared in loops and conditionals are not scoped 
# the act like global variables and can be accessed outside the loop

for char in 'OCTOPUS':
    color = 'magenta'
    print(char)



if True:
    person = 'boy'

# In here we can access color and person outside the loop, though they're declared inside the loop
print(color) 
print(person)
