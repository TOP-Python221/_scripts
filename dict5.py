morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
		'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
		'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
		'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
		'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
		'3': '...--', '4': '....-', '5': '.....', '6': '-....','7': '--...', 
		'8': '---..', '9': '----.', ' ': ''}

morse_invert = {}
for k, v in morse.items():
    morse_invert[v] = k

morse_word = input('morse message (sep letters by space): ').split() + ['']
msg_out = ''

for key in morse_word:
    msg_out += morse_invert[input_code].lower()
print(f'"{msg_out}"')
