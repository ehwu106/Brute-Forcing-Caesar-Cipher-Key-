def brute_force_cipher(message):
    for num in range(1,26):
        decrypted = ""
        for letter in message:
            if ord(letter)==32:
                decrypted+=" "
                continue
            ascii_shifted = ord(letter)-num
            if letter.isupper() and ascii_shifted < 65:
                ascii_shifted = 91 - (65 - ascii_shifted)
            elif letter.islower() and ascii_shifted < 97:
                ascii_shifted = 123 - (97 - ascii_shifted)
            decrypted+=chr(ascii_shifted)
        print('Brute Forcing key #'+str(num)+' | value: '+decrypted)

message = input('Enter the encrypted message: ')
brute_force_cipher(message)