"""
Метод: Translate
"""

morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', ord('D'): '-..', ord('E'): '.', 'F': '..-.',
              'G': '--.', ord('H'): '....', 'I': '..', 'J': '.---', 'K': '-.-', ord('L'): '.-..',
              'M': '--', 'N': '-.', ord('O'): '---', 'P': '.--.', 'Q': '--.-', ord('R'): '.-.',
              'S': '...', 'T': '-', 'U': '..-', 'V': '...-', ord('W'): '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
              '8': '---..', '9': '----.'}

# string = 'Hello world'
string = 'tats'

prepare = []
for ch in string:
    prepare.append(ch.upper().translate(morze_dict))
translated = ' | '.join(prepare)
print(translated)

# data_str = "зюбщ"
# symbol_translate = {
#     ord('з'): 'z',
#     ord('ю'): 'u',
#     ord('б'): 'b',
#     ord('щ'): 'shch',
# }
# new_str = data_str.translate(symbol_translate)
# print(new_str)
