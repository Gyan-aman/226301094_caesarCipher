#make a function for caesar copher
def caesar_cipher(text, shift):
    """
    Encrypts/Decrypts a text using the Caesar Cipher.

    Parameters:
    - text (str): The text to be encrypted/decrypted.
    - shift (int): The number of positions to move the letters.

    Returns:
    str: The encrypted/decrypted text.
    """
    result = ""  # We start with an empty result string

    for char in text:
        # We look at each letter in the text

        # If it's a capital letter
        if char.isupper():
            # Move the letter in the alphabet, and make sure it stays a capital letter
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # If it's a lowercase letter
        elif char.islower():
            # Move the letter in the alphabet, and make sure it stays a lowercase letter
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            # If it's not a letter, keep it as it is (like spaces or punctuation)
            result += char

    return result  # We now have the encrypted/decrypted text

# Taking user input
text = input("Enter the secret message: ")
shift = int(input("Enter how many places to shift the letters: "))

# Choosing between making a secret code or decoding
action = input("Type 'code' to make a secret code or 'decode' to read a secret code: ")

# Doing what the user asked for
if action.lower() == 'code':
    secret_code = caesar_cipher(text, shift)
    print(f"Here is your secret code: {secret_code}")
elif action.lower() == 'decode':
    decoded_message = caesar_cipher(text, -shift)  # Using a negative shift to decode
    print(f"Shhh... The secret message says: {decoded_message}")
else:
    print("Oops! I didn't understand. Type 'code' or 'decode', please.")