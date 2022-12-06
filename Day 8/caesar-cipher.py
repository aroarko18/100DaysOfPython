alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message = text, difference = shift):
    encrypt_text = []
    for letter in message:
        position = alphabet.index(letter)
        position = position + difference
        
        encrypt_message = alphabet[position]
        encrypt_text.append(encrypt_message)    
    print("The encoded text is " + ''.join(encrypt_text))

def decrypt(message = text, difference = shift):
    decrypt_text = ''
    for letter in message:
        position = alphabet.index(letter)
        position = position - difference

        decrypt_message = alphabet[position]
        decrypt_text = decrypt_text + decrypt_message
    print(f"The decoded text is {decrypt_text}")

if direction == "encode":
    encrypt()
elif direction == "decode":
    decrypt()
else:
    print("Sorry! Your direction is wrong.")