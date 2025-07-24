# Alexandre Cheminat - z5592322 - 27/06/2025
# This script embeds and extracts data in images using LSB steganography

from PIL import Image
import numpy as np

def bytesToBits(data):
    return ''.join(f'{byte:08b}' for byte in data)

def bitsToBytes(bits):
    return bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))

# Reference: https://github.com/RobinDavid/LSB-Steganography
def embedMessageInImage(imagePath, dataBytes, outputPath):
    img = Image.open(imagePath)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    pixels = np.array(img)
    h, w, _ = pixels.shape

    # Flatten pixel array to 1D list of channels
    flatPixels = pixels.flatten()

    messageBits = bytesToBits(dataBytes)
    messageLen = len(messageBits)

    # Store message length as 32 bit integer at start (big endian)
    lengthBits = f'{messageLen:032b}'
    totalBits = lengthBits + messageBits

    if len(totalBits) > len(flatPixels):
        raise ValueError("Message too large to fit in image")

    # Modify the LSBs of pixels
    for i, bit in enumerate(totalBits):
        flatPixels[i] = (flatPixels[i] & ~1) | int(bit)

    newPixels = flatPixels.reshape((h, w, 4))
    newImg = Image.fromarray(newPixels.astype('uint8'), 'RGBA')
    newImg.save(outputPath)

def extractMessageFromImage(imagePath):
    img = Image.open(imagePath)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    pixels = np.array(img).flatten()

    lengthBits = ''.join(str(pixels[i] & 1) for i in range(32))
    messageLen = int(lengthBits, 2)

    # Read message bits
    messageBits = ''.join(str(pixels[i] & 1) for i in range(32, 32 + messageLen))
    return bitsToBytes(messageBits)
