# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

encode_table = {"A": "M",
"B": "N",
"C": "B",
"D": "V",
"E": "C",
"F": "X",
"G": "Z",
"H": "L",
"I": "K",
"J": "J",
"K": "H",
"L": "G",
"M": "F",
"N": "D",
"O": "S",
"P": "A",
"Q": "P",
"R": "O",
"S": "I",
"T": "U",
"U": "Y",
"V": "T",
"W": "R",
"X": "E",
"Y": "W",
"Z": "Q"}

# def encode(s):
#     encoded_string = ''

#     s = s.upper()
#     for character in s:
#         if character not in encode_table:
#             encoded_string += character
#         else:
#             scrambled_character = encode_table[character]
#             # build return string
#             encoded_string += scrambled_character
    
#     return encoded_string

decode_table = {v : k for k, v in encode_table.items()}

def encode(s):
    r = ''

    for c in s:
        r += encode_table[c]

    return r
print(encode('HELLOWORLD'))

def decode(s):
    r = ''

    for c in s:
        r += decode_table[c]
    
    return r

print(decode('LCGGSRSOGV'))



decode_table = {}

# decode_table = {v:k for k, v in encode_table.items()}

# def build_decode(encoding_table):
#     for key, value in encoding_table.items():
#         decode_table[value] = key


# def decode(s):
#     decoded_string = ''

#     s = s.upper()
#     for character in s:
#         if character not in decode_table:
#             decoded_string += character
#         else:
#             unscrambled_character = decode_table[character]
#             # build return string
#             decoded_string += unscrambled_character

#     return decoded_string