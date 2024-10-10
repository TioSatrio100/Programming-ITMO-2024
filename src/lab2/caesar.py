def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = ord("A") if char.isupper() else ord("a")

            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
           
            new_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            plaintext.append(new_char)  
        else:
            plaintext.append(char)  

    return ''.join(plaintext)  
