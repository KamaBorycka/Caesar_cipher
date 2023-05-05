from alphabet import alphabet
from art import logo

playing = True

print(logo)

while playing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        modulus = shift % 26
        shift = modulus

    def ceasar(user_text, user_shift, user_direction):
        decode_or_code = ""

        for character in user_text:
            if character in alphabet:
                index_alphabet = alphabet.index(character)
                if user_direction == "encode":
                    letter_code = alphabet[index_alphabet + user_shift]
                    decode_or_code += letter_code
                else:
                    letter_decode = alphabet[index_alphabet - user_shift]
                    decode_or_code += letter_decode
            else:
                decode_or_code += character
        print(f"The {user_direction}d text is {decode_or_code}")

    ceasar(user_text=text, user_shift=shift, user_direction=direction)

    decision = input("Do you want to restart cipher program? ")

    if decision == "no":
        playing = False
        print("Goodbye")
