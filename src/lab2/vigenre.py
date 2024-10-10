def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    # PUT YOUR CODE HERE
    ciphertext = ""
    keyword_repeated = ""
    keyword_length = len(keyword)

    keyword_index = 0
    for char in plaintext:
        if char.isalpha():
            keyword_repeated += keyword[keyword_index % keyword_length].upper()
            keyword_index += 1
        else:
            keyword_repeated += char

    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():
            shift = ord(k_char) - ord('A')
            base = ord('A') if p_char.isupper() else ord('a')
            new_char = chr((ord(p_char) - base + shift) % 26 + base)
            ciphertext += new_char
        else:
            ciphertext += p_char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE

    return plaintext