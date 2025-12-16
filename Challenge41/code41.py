# Coding Challenge 41
# Convert number to words digit by digit

# Dictionary mapping digits to words
digit_words = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

# Input number as string
number = input("Enter a number: ")

# Convert each digit to word
words = [digit_words[digit] for digit in number]

# Join and display
output = " ".join(words)
print(output)
