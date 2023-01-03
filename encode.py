def encrypt(message,shift):
    encrypted = ""
    for letter in message:
        if ord(letter)==32:
            encrypted+=" "
            continue
        ascii_shifted = ord(letter)+int(shift)
        if letter.isupper() and ascii_shifted > 90:
            ascii_shifted = 64+(ascii_shifted - 90)
        elif letter.islower() and ascii_shifted > 122:
            ascii_shifted = 96+(ascii_shifted - 122)
        letter_shifted= chr(ascii_shifted)
        encrypted+=letter_shifted
    return encrypted

message = input('Enter your message: ')
shift = input('key (how much you want to shift): ')
print('Encrypted message: '+encrypt(message, int(shift)))