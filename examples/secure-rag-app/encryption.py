from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode())

def decrypt(token):
    return cipher.decrypt(token).decode()
