# Alexandre Cheminat - z5592322 - 19/06/2025
# This script encrypts and decrypts data using AES-256 encryption

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# PBKDF2 (Password-Based Key Derivation Function 2)
# Reference: https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#pbkdf2hmac
def deriveKeyAndIV(password: str, salt: bytes) -> tuple[bytes, bytes]:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=48,
        salt=salt,
        iterations=100_000,
    )
    keyIv = kdf.derive(password.encode())
    return keyIv[:32], keyIv[32:]

def generateKeyIv():
    key = os.urandom(32)
    iv = os.urandom(16)
    return key, iv

# Reference: https://ssojet.com/encryption-decryption/aes-256-in-python/
def encryptMessage(data: bytes, key: bytes, iv: bytes) -> bytes:
    padder = padding.PKCS7(128).padder()
    paddedData = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(paddedData) + encryptor.finalize()

def decryptMessage(encryptedData: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded = decryptor.update(encryptedData) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()
