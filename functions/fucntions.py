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

version2_count_vowels('abcdoefi')