#!/usr/bin/python3
from Crypto.Cipher import AES
key = b"4N3tH3rSt4T1cK3y"
aesObj = AES.new(key, AES.MODE_ECB)
encrypted = aesObj.encrypt(flag)
print(f"encrypted : {encrypted}")
# encrypted : 'J\x96Qek/ \x8e\x17r\x14q\x90\x16\xde\xd3\xeez74\xab\xe7\xd8T4\xae\t\xcaW\x97\x0ck\x05\xfa\x08\xe3\x95~\x1c\xd2?W~0\xbd\x0ca\xf0'
