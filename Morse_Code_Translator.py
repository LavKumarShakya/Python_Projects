# Morse Code Translator

morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ', ': '--..--', '. ': '.-.-.-', '? ': '..--..', '/ ': '-..-.', 
        '- ': '-....-', '(' : '-.--.', ') ': '-.--.-'
    }
def encrypt_message(message):
    message = message.upper()
    encrypted_message = ''
    for letter in message:
        if letter != ' ':
            encrypted_message += morse_code[letter] + ' '
        else:
            encrypted_message += ' '
    return encrypted_message[:-1]

def decrypt_morse_code(message):
    message += ' '*2
    decrypted_message = "" 
    word = ""
    for i in range(len(message)-1):
        if message[i] == ' ':
            for key, value in morse_code.items():
                if word == value:
                    decrypted_message += key
                    word = ""
            if message[i+1] == ' ':
                decrypted_message += ' '
                word = ""
            else:
                continue
        else:
            word += message[i]
    return decrypted_message

message = "LEARNING MORSE CODE IS FUN AND USEFUL FOR COMMUNICATION"
code1=".-.. . .- .-. -. .. -. --.  -- --- .-. ... .  -.-. --- -.. .  .. ...  ..-. ..- -.  .- -. -..  ..- ... . ..-. ..- .-..  ..-. --- .-.  -.-. --- -- -- ..- -. .. -.-. .- - .. --- -."
print("Encrypted message: ", encrypt_message(message))
print("Decrypted message: ", decrypt_morse_code(code1))


