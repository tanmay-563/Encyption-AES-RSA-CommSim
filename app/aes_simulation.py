from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt(message, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_msg = pad(message).encode()
    encrypted = cipher.encrypt(padded_msg)
    return base64.b64encode(encrypted).decode()

def decrypt(ciphertext, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(ciphertext)
    decrypted = cipher.decrypt(decoded)
    return decrypted.decode().strip()

def hmac_sha256(message: str, key: bytes) -> str:
    hmac = HMAC.new(key, message.encode(), SHA256)
    return base64.b64encode(hmac.digest()).decode()

def encrypt_with_hmac(message, aes_key, hmac_key):
    encrypted_message = encrypt(message, aes_key)
    hmac_value = hmac_sha256(encrypted_message, hmac_key)
    return encrypted_message, hmac_value

def decrypt_with_hmac(encrypted_message, aes_key, hmac_key):
    # First, verify HMAC
    expected_hmac = hmac_sha256(encrypted_message, hmac_key)
    decrypted_message = decrypt(encrypted_message, aes_key)
    return decrypted_message, expected_hmac
