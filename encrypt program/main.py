def encrypt(text, shift):
    result = ''

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted_char
        else:
            result += char  #if char is not given

    return result

plain_text = input("Enter the text to encypt: ")
shift_value = int(input("Enter the shift value: "))

encrypted_text = encrypt(plain_text, shift_value)
print("Encrypted text: ", encrypted_text)