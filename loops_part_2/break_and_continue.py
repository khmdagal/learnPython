
word_1 = "supercalifragilisticexpialidocious";
word_2 = 'FATCAT';


# =========   BREAK  ===========
# this iteration will stop when the it hits letter C and will not go further
for letter in word_1:
    if letter == 'c':
        break
    print(letter)

print("=========================")

# =========   CONTINUE  ===========
# If the letter equals 'A' the iteration will scape and goes next letter and will print if it is not A
for letter in word_2:
    if letter == 'A':
        continue
    print(letter)

print("=========================")

# In this iteration we are expecting the no vowels will be printed just only consonants
for char in word_1:
    if char in 'aioue':
        continue
    print(char)

print("=========================")