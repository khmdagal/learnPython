# str.lower() # make the string lower case
# str.upper() # make the string upper case
# str.capitalize() # make the string Capitalize first character
# str.startswith()
# str.endswith()
# str.find()
# str.replace()
# str.join()
# str.lstrip()
# str.removeprefix()
# str.removesuffix()
# str.rfind()
# str.rindex()
# str.rjust()
# str.split()
# str.strip()
# str.swapcase()
# str.title()

# ===========
# The difference of the str.title() and str.capitalize() 
# ===========

# string = 'hello world'

# print("str.title() ===>>>",string.title());      # output: Hello World 
# print("str.upper() ===>>>",string.capitalize())  # output: Hello World


# ===== Strip() and replace =========

races = '3miles 5miles 10miles'
# races.replace('miles','kilomiters')
print(races) # this will not change the origin of the races varaible and prints out '3miles 5miles 10miles'

# Now I am storing a new varialble 
replaced_races = races.replace('miles','kilomiters')
print(replaced_races)
