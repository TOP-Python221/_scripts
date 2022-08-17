morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
		'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
		'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
		'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
		'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
		'3': '...--', '4': '....-', '5': '.....', '6': '-....','7': '--...', 
		'8': '---..', '9': '----.', ' ': ''}

morse_word = input('morse message (sep letters by space): ').split()
msg_out = ''

for input_code in morse_word:
    for letter, code in morse.items():
        if input_code == code:
            msg_out += letter.lower()
print(msg_out)
