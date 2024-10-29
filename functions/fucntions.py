# this function should only return the number of vowels in the string

def count_vowels(word):
    vowels_array = []
    for char in word:
        if char in 'aeiou':
            vowels_array.append(char)
    
    
    return len(vowels_array)

number_of_vowels = count_vowels('abcdefi')

# print(number_of_vowels)

# refactored version of the count_vowel function

def version2_count_vowels(word):
    count = 0

    for char in word:
        if char in 'aeiou':
            count += 1
    print(count)
    return count

# version2_count_vowels('abcdoefi')


#  functions with default arguments
def greet(name='world'):
    return f'Hello, {name}'
# print(greet())
# print(greet('John'))


# function with only required parameter
def slugify(msg):
    return msg.lower().strip().replace(' ', '-')

print(slugify('Hello lovely world'))

# Function with default value and required parameter
# Tip to remember is that the  order of parameters matters 
# when using default parameter and it should come last 

def slugify_default_value(msg, separate='**'):
    return msg.lower().strip().replace(" ", separate)
print(slugify_default_value('Hello lovely world'))