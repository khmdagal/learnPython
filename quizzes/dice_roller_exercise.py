from random import randint

dices = int(input('How many dice are we rolling? '))
sides = int(input('How many sides on each die? '))


while True:
    result = '|'
    for die in range(dices):
        role = randint(1,sides)
        result += f"{role}|"
    print(result)
    reply = input('Enter q to quit ')
    if reply == 'q':
        break


# ======= Exercise Instructions ===========

# Dice Roller
# Create a script that rolls dice for a user.  When the script runs, it should ask a user how many dice they want to roll and how many sides each die will have.  Then it randomly rolls those dice and prints the result.  Every time a user hits Enter, the dice are rolled again.  If a user every enter “q”, then the script quits and stops running!
# Hints:
# use randint() to generate the dice rolls. Remember, you need to import it from random
# start by rolling a single die before rolling multiple
# you’ll need to use nested loops!
# Here’s an example of the script in action where the user wanted three 6-sided dice:
# How many dice are we rolling? 3
# How many sides on each die? 6
# |5|1|4|
# Roll again? ('q' to quit) 
# |5|3|1|
# Roll again? ('q' to quit) 
# |2|4|1|
# Roll again? ('q' to quit) q
# ​
# The following example rolls two 20-sided die:
# How many dice are we rolling? 2
# How many sides on each die? 20
# |19|20|
# Roll again? ('q' to quit) 
# |6|1|
# Roll again? ('q' to quit) 
# |6|11|
# Roll again? ('q' to quit) 
# |2|13|
# Roll again? ('q' to quit) q