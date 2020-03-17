


import string

def compute_ascii_passwords() -> list:
    passwords = []
    for letter1 in range(ord('a',ord('z'))):
        for letter2 in range(ord('a', ord('z'))):
            for letter3 in range(ord('a', ord('z'))):
                passwords.append(letter1+letter2+letter3)
    return passwords

def check_password(password:int, encrypted_string:list) -> bool:
    decrypted_chars = [chr(num ^ password) for num in encrypted_string]
    decrypted_string = ""
    for char in decrypted_chars: decrypted_string+=char
    print(decrypted_string)
    commom_words = ["and", "the", "or"]
    print(commom_words[0])
    for word in commom_words:
        if word in decrypted_string:
            return True
    return False



    

