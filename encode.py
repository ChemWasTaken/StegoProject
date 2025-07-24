# Alexandre Cheminat - z5592322 - 4/07/2025
# This script encodes a message into an image using LSB and AES encryption

import os
from encryption import encryptMessage, deriveKeyAndIV
from stego import embedMessageInImage

def encode(imagePath, message, password, outputPath):
    salt = os.urandom(16)
    key, iv = deriveKeyAndIV(password, salt)
    encrypted = encryptMessage(message.encode('utf-8'), key, iv)
    combined = salt + encrypted

    embedMessageInImage(imagePath, combined, outputPath)
    print("Message embedded")

password = input("Enter password: ")
message = input("Enter a message to encode: ")
name = input("Enter input/output filename: ")

encode("input/" + name, message, password, "output/" + name)
