# Simple-Encryption-Tool

> A simple tool to automate basic encryption/decryption methods. Built to practice python modules such as hashlib, and base64

## Overview

- It can encrypt and decrypt text from Binary, Base64, Morse, Ceaser Cipher, and can produce a SHA256 hash.
- Built to have practice with nested one-liners, and encryption methods
- It might be useful for someone who wants to see basic one liners, and the correct usage of character_maps.

## Features

- Conversion — Converts plaintext to Binary, Base64, Morse
- Encryption — Can do a basic Ceaser Cipher, provided a key
- Decryption — Can undo the Ceaser Cipher, provided the key
- Hashing — Can find the SHA256 hash of some text.

## Tech Stack

- **Language:** Python
- **Libraries:** hashlib, base64

## Getting Started

### Prerequisites

- Python 3.11.3
- Requires hashlib and base64 modules

### Installation

```bash
git clone https://github.com/A-Proper-programmer/Simple-Encryption-Tool
cd Simple-Encryption-Tool
```

Install dependencies if required:

```bash
pip install hashlib
```

### Usage

Run the program by opening it either in python or in a shell with the following command: 

```bash
python Enkryptor.py
```


## Example

```text
Example input: 

Enter the text to encrypt/decrypt : *Hello*
[1] Ceaser Cipher
[2] Base64
[3] Binary
[4] Morse
[5] SHA-256 (One-way)
Enter the mode : *1*
Encrypt or Decrypt [e/d] : *e*
Enter number of shifts to the right : *5*

Example output:

Mjqqt
Press Enter to continue...
```


## Project Structure

```text
Simple-Encryption-Tool/
├── Enkryptor.py
└── README.md
```

## What I Learned

- I learnt how translate tables workes, and how to use inline statements efficiently.
- While testing, the script couldnt handle the error if the inputs were wrong.
- I used try-except and if statements to handle them.

## Limitations

- It is possible to enter values other than *e*,*d*, when it asks for "Encrypt or Decrypt".
- Has limited functions.

## Future Improvements

- [ ] Make Errors more visible.
- [ ] Fix the "e,d" problem
- [ ] Add more encryption
