#EXAMPLE TESTING
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import random


hash = SHA256.new().hexdigest()
#print(hash)
key = 'ABCDEFGHIJKLM123'
iv = 'IVIVIVIVIVIVIVIV'
obj = AES.new(key,AES.MODE_CBC,iv)
message = "The answer is no" #fixed data block size of 16 bytes
ciphertext = obj.encrypt(message)
obj2 = AES.new(key, AES.MODE_CBC,iv)
print(obj2.decrypt(ciphertext))

value = random.choice(['dogs','doggo','doge'])
print(value)
