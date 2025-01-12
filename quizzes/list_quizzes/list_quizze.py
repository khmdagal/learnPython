# ===  Question =====
# Given this list:

# seeds = ["beans", "peas", "sunflowers"]
# How would I update it to look like this:

# ["beans", "peas", "plums", "sunflowers"]
# ==== Solution =====

seeds = ["beans", "peas", "sunflowers"]
# seeds[2] = "plums" # ['beans', 'peas', 'plums'] this is replacing the value at index 2 with plums
# seeds.append(2, "plums") # TypeError: append() takes exactly one argument (2 given)
seeds.insert(2, 'plums')
# we achieved the desired output by using the insert method
# it inserts the new value to the index that is specified
# And one thing to remember is that all the other elements are shifted by one index or more if more elements are inserted
# so for performance reasons, it's better to use the append method if you want to add a value at the end of the list

print(seeds) # ['beans', 'peas', 'plums', 'sunflowers']


# ============ Question 2 =============
# Given the following list:

# greens = ["kale", "chard", "spinach", "arugula"]
# Which of the following slices results in ['chard', 'spinach'] 
#  greens[1] or greens[1:] or greens[3:] or greens[1:4] or greens[1:3]
# === Solution =====
greens = ["kale", "chard", "spinach", "arugula"]
print(greens)
print(greens[1:3])


# ============ Question 3 =============
#After the following code runs:

# roosters = ['rusty', 'tango', 'roo paul']
# diner = roosters.pop()
# What are the values of roosters and diner ?


# === Solution =====
roosters = ['rusty', 'tango', 'roo paul']
dinner = roosters.pop()
print(dinner)

# === question 4 ======
# Given this list:

# users = ['esteban', 'fernando','lando','pierre', 'yuki']
# Which of the following answers would remove 'lando' from users

# === Solution =====    
users = ['esteban', 'fernando','lando','pierre', 'yuki']
# print("====>>>",users)
# users.remove(2) # TypeError: 'lando' is an invalid keyword argument for pop()
# print("====>>>",users)


# === question 5 ======
# Given this colors list:

# colors = ["red", "orange", "yellow", "green"]
# Which of the following loops results in the following being printed out (notice the order!):

# green
# yellow
# orange
# red

# === Solution =====
colors = ["red", "orange", "yellow", "green"]

index = len(colors) -1
print(index)

while index >= 0:
    print(colors[index])
    index -= 1
