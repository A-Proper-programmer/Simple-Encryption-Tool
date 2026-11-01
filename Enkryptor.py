import base64, hashlib

def ceaser_c(text, mode):
    while True:
        try: key = int(input("Enter number of shifts to the right : "))%26
        except ValueError: print("Enter a number")
        else: break

    shifted = list("abcdefghijklmnopqrstuvwxyz")
    if mode=="d": key=26-key

    for _ in range(key):
        shifted.append(shifted.pop(0))
    alphabets = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shifted += [i.upper() for i in shifted]

    char_map = dict(zip(alphabets, shifted))
    return text.translate(str.maketrans(char_map))

def base_64(text, mode):
    text_bytes = text.encode('utf-8')
    final_bytes = base64.b64encode(text_bytes) if mode == "e" else base64.b64decode(text_bytes)
    return final_bytes.decode('utf-8')

def binary(text, mode):
    final = []
    if mode=="e":
        final += [str(format(ord(i), "08b"))+" " for i in text]
        final = ''.join(final)
        return final
    if mode=="d":
        for i in text:
            if i==" ": continue
            if i not in ["0", "1"]: print("Give a correct binary sequence with only spaces, 0s and 1s."); return
            final += [i]
        if len(final)%8: print("Needs binary with length mod 8"); return
        final_text = ""
        for _ in range(len(final)//8):
            final_text += chr(int("0b"+''.join(final[:8]), base=2))
        return final_text

def morse(text, mode):
    # GOOGLED
    MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'}
    if mode=="e": return str(" ".join(text.upper())).translate(str.maketrans(MORSE_CODE_DICT)).replace("   ", " / ")
    if mode == "d":
        final = ""
        reverse = {value:key for key, value in MORSE_CODE_DICT.items()}
        reverse["/"] = " "
        for i in text.split():
            final += reverse[i]
        return final


inp_text = input("Enter the text to encrypt/decrypt : ")
while True:
    type = input("[1] Ceaser Cipher \n[2] Base64 \n[3] Binary \n[4] Morse \n[5] SHA-256 (One-way)\nEnter the mode : ")
    try: type = int(type)
    except ValueError: print("Type the mode. Eg: 1, 2, etc")
    else:
        if type not in [1,2,3,4,5]: print("Type an existing mode [1,2,3,4,5].")
        else: break 

if type-5: func = input("Encrypt or Decrypt [e/d] : ")

if type == 1: print(ceaser_c(inp_text, func))
elif type == 2: print(base_64(inp_text, func))
elif type == 3: print(binary(inp_text, func))
elif type == 4: print(morse(inp_text, func))
elif type == 5: print(hashlib.sha256(inp_text.encode('utf-8')).hexdigest())
        
input("Press Enter to continue...")
