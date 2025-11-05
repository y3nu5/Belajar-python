alphabet =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]


# version 1
# def encrypt(text, shift):
#     text_encrypted = ""
#     for char in text:
#         position = alphabet.index(char)
#         new_position = position + shift
#         if new_position > 25:
#             new_position = new_position % 26
#         print(new_position)
#         new_char = alphabet[new_position]
#         text_encrypted += new_char
#     print(f"The encoded text is {text_encrypted}")

# encrypt(text, shift)
    
# def decrypt(text, shift):
#     text_decrypted = ""
#     for char in text:
#         position = alphabet.index(char)
#         new_position = position - shift
#         new_char = alphabet[new_position]
#         text_decrypted += new_char
#     print(f"The decoded text is {text_decrypted}")


def caesar(originaltext, shiftedamount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
                shiftedamount *= -1
                
    for char in originaltext:

        if char not in alphabet:
            output_text += char
        else:
            shifted_position = alphabet.index(char) + shiftedamount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"The {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(originaltext=text, shiftedamount=shift, encode_or_decode=direction)

    input_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if input_continue == "no":
        should_continue = False
        print("finished")
