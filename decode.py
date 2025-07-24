# Alexandre Cheminat - z5592322 - 4/07/2025
# This script decodes a message from an image using LSB and AES decryption

from encryption import decryptMessage, deriveKeyAndIV
from stego import extractMessageFromImage

def decode(imagePath, password):
    try:
        combined = extractMessageFromImage(imagePath)
        salt = combined[:16]
        encrypted = combined[16:]

        key, iv = deriveKeyAndIV(password, salt)
        decrypted = decryptMessage(encrypted, key, iv)
        return "Decrypted message: " + decrypted.decode('utf-8')
    except Exception:
        if imagePath.lower().endswith(("jpg", "webp", "heif")):
            return "Error: The program does not support lossy file formats"
        else:
            return f"Error: The password given is incorrect"

password = input("Enter password: ")
name = input("Enter name of file to decode: ")
print(decode("output/" + name, password))
