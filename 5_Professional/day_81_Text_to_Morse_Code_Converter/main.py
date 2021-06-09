# Text to Morse Convertor
from tools import clear
from art import logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = ['.', ',', '?', '\'', '!', '/', '(', ')', '&', ':', '=', '+', '-', '_', '"', '$', '@']
morse_letters = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
morse_numbers = ['-----', '.----', '..---', '...--', '....-', '......', '-....', '--...', '---..', '----.']
morse_punctuation = ['.-.-.-', '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.']

clear()
print(logo)
print("Welcome to the Text to Morse Converter!")
user_text = input("text to convert: ").lower()

morse = ""

for _ in user_text:
    if _ in letters:
        idx = letters.index(_)
        morse += f"{morse_letters[idx]} "
    elif _ in numbers:
        idx = numbers.index(_)
        morse += f"{morse_numbers[idx]} "
    elif _ in punctuation:
        idx = punctuation.index(_)
        morse += f"{morse_punctuation[idx]} "
    elif _ == ' ':
        morse += '    '

print(f"Here is the morse conversion: {morse}")
