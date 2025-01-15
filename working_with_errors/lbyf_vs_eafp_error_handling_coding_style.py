# LBYF vs EAFP

# ======  LBYF  ========
# LBYF standand for  'Look Before Your Leap' and is coding style
# where you explicitly test for pre-conditions before making calls or 'leaping'.
# Characterized by lots of if statements


year = input('Enter a year')
if year.isnumeric(): # This is where looking takes place before executing the rest of the code.
    year = int(year)
else:
    year = 2025


# ======== EAFP  =======
# EAFP stands for  'Easier to Ask for Forgiveness then Permission' and is coding style
# Assume things exist or will work, and catch exceptions if you're wrong.
# Characterized lots of try/except blocks.

try:
    year2 = input('Enter a year') # Assuming it will work
except ValueError: # Catch exceptions if you're wrong
    year = 2025


