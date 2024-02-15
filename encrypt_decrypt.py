alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
       position = alphabet.index(letter)
       new_position = position + shift
       new_letter = alphabet[new_position]
       cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift=shift)