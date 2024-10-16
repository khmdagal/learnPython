
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)

print('========================================')
# Write a while loop that does the same thing!

count = 0
while count < len(word):
    print(word[count])
    count = count + 1

print('========================================')

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)

number = 100

while number < 141:
    print(number)
    number+=2
print('========================================')
# Write a for loop that does the same thing (with range())

for num in  range(100,141,2):
    print(num)


#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:

phrase = ''

while phrase != 'sillygoose':
   phrase = input('Please say (sillygoose) ')
   if phrase == "sillygoose":
        print(f"""That is goooooooood
         You said {phrase}
         """)
