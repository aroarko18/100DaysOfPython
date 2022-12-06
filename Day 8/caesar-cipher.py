alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if not char in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

import art
print(art.logo)

should_continue = True
while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    


    still_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if still_continue == "yes":
            should_continue
    elif still_continue == "no":
        print("Good bye")
        should_continue = False
    else:
        print("Sorry input error!\nGood bye.")
        should_continue = False
        
    