Practical No: 6

Lab Assignment-1

Develop an application which asks the user to enter a string and prints its statistics as:

a) Number of Vowels

b) Number of Consonants

c) Number of Spaces

d) Number of Lowercase Letters

# Taking input from user
text = input("Enter a string: ")

# Initialize counters
vowels = 0
consonants = 0
spaces = 0
lowercase = 0

# Define vowels
vowel_set = "aeiouAEIOU"

# Loop through each character
for ch in text:
    if ch in vowel_set:
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    if ch == " ":
        spaces += 1
    if ch.islower():
        lowercase += 1

# Display results
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of spaces:", spaces)
print("Number of lowercase letters:", lowercase)

Lab Assignment-2

Design a function that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the

program Practice makes perfect

Then, the output should be. PRACTICE MAKES PERFECT

CODE 

# Function definition
def convert_to_upper():
    text = input("Enter a sentence: ")
    result = text.upper()
    print("Output:", result)

# Function call
convert_to_upper()

