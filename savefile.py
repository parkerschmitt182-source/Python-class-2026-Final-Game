def read_game(shift):
    
    def encrypt(text, shift):
        shift = int(shift/13192957315647357)
        print(shift)
        result = ""
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        return result
    def decrypt(text, shift):
        return encrypt(text, shift*-1)
    with open("Carlo_Acutis.nextgensavefile", "r") as file:
          encrypted = file.read()
          return(decrypt(encrypted, shift))



def save_game(data):


    def encrypt(text, shift):
        shift = int(shift/13192957315647357)
        print(shift)
        result = ""
        for char in text:
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                shifted = (ord(char) - base + shift) % 26
                result += chr(base + shifted)
            else:
                result += char
        return result
    def decrypt(text, shift):
        return encrypt(text, -shift)
    message = data
    encrypted = encrypt(message, 65964786578236785)
    decrypted = decrypt(encrypted, 65964786578236785)

    print(encrypted)  # Khoor Zruog!
    print(decrypted)  # Hello World!
    with open("Carlo_Acutis.nextgensavefile", "w") as file:
          file.write(str(encrypted))
