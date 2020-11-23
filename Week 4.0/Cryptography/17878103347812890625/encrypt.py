#!/usr/share/python3
import random

filename = "REDACTED"
extension = "png"

with open('.'.join([filename, extension]), 'rb') as handle:
	content = handle.read()

key = [ random.randint(1,255) for i in range(8) ]

encrypted = b""
for i in range(len(content)):
	encrypted += (content[i] ^ key[i%len(key)]).to_bytes(1, 'little')

with open('encrypted.'+extension, 'wb') as handle:
	handle.write(encrypted)
