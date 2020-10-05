#!/usr/bin/python3

flag = "REDACTED"
key = "REDACTED"
keyIndex = 0
enc = ""

for c in flag:
	if ord(c) >= ord('A') and ord(c) <= ord('Z'):
		enc += chr( (( ord(c) - ord('A') + (ord(key[keyIndex]) - ord('a')) ) % 26) + ord('A'))
	elif ord(c) >= ord('a') and ord(c) <= ord('z'):
		enc += chr( (( ord(c) - ord('a') + (ord(key[keyIndex]) - ord('a')) ) % 26) + ord('a'))
	else:
		enc += c
	
	keyIndex += 1
	if keyIndex == len(key):
		keyIndex = 0

print(enc)
#YzkwfmekLjFwlbrxWyefLprYdcev