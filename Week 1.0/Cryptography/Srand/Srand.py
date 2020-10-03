import random

key = "SuP3rs3cR3tK3y"

random.seed(key)
flag = "REDACTED"

encrypted = ""
for c in flag:
	encrypted += chr(ord(c) ^ random.randint(1,100))

with open('encrypted.txt', 'w') as f:
	f.write(encrypted)
