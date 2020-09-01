import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
def encrypt(data,password):
          password = password.encode()
          salt = b'keep_Shredding_the_files'
          kdf = PBKDF2HMAC(
          algorithm=hashes.SHA256(),
          length=32,
          salt=salt,
          iterations=100000,
          backend=default_backend()
                         )
          key = base64.urlsafe_b64encode(kdf.derive(password))
          f = Fernet(key)
          token = f.encrypt(data)
          return token
def decrypt(cipher_text,password):
          password = password.encode()
          salt = b'keep_Shredding_the_files'
          kdf = PBKDF2HMAC(
          algorithm=hashes.SHA256(),
          length=32,
          salt=salt,
          iterations=100000,
          backend=default_backend()
                         )
          key = base64.urlsafe_b64encode(kdf.derive(password))
          f = Fernet(key)
          return f.decrypt(cipher_text)

#print(encrypt(b'sadasdasdasd',b'yash'))
#print(decrypt(b'gAAAAABeG_o1NalNb7UPwfOFtXVxr7uooaSdUdIJGXc0AgFlUuHCodu1TTaJUlG71MyQ4uevJ24bY_5FuRbR_8z_LG5Zgke9bA==',b'yash'))
