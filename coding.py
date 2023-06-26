def encrypt(encrypted_text, n):
    for _ in range(n):
        encrypted_text = encrypted_text[1::2]+encrypted_text[0::2]
    return encrypted_text

def decrypt(encrypted_text, n):
    if not encrypted_text:
        return encrypted_text
    encrypted_text = list(encrypted_text)
    for _ in range(n):
        encrypted_text[1::2],encrypted_text[::2] =encrypted_text[:len(encrypted_text)//2], encrypted_text[len(encrypted_text)//2:]

    return ''.join(encrypted_text)