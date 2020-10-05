#!/usr/bin/python3

flag = "REDACTED"
key = "REDACTED"

enc = ""
for c in flag:
	if ord(c) >= ord('A') and ord(c) <= ord('Z'):
		enc += chr( (( ord(c) - ord('A') + key ) % 26) + ord('A') )
	elif ord(c) >= ord('a') and ord(c) <= ord('z'):
		enc += chr( (( ord(c) - ord('a') + key ) % 26) + ord('a'))
	else:
		enc += c

print(enc)
#ZSUCDSTK{UsWkSj_Ak_CaFv_Gx_AfKwUmJw}