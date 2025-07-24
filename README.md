# StegoProject

**COMP6841 Final Project – Steganography and Encryption Tool**  
Created by Alexandre Cheminat (z5592322)

## Overview

This tool securely hides messages inside non-lossy images using a combination of AES-256 encryption and LSB (Least Significant Bit) steganography. It ensures that even if the hidden data is extracted, it remains encrypted and unreadable without the correct password. All images need to be placed in the `input` folder in order to be processed.

The project is split into two main components:

- `encode.py` – Encrypts and embeds a message inside an image.
- `decode.py` – Extracts and decrypts the hidden message from an image.

---

## Features

- AES-256 encryption with PBKDF2 key derivation
- LSB steganography on RGBA images
- Automatic conversion of input images to support transparency
- Message size and format validation
- Approximate capacity: 4 bits per pixel (RGBA)

---

## Requirements

- Python 3.9+
- Packages:
  - `cryptography`
  - `pillow`
  - `numpy`

Install dependencies via:

```bash
pip install -r requirements.txt
