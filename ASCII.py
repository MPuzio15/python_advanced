print(chr(67))
key=3
text = "A"
convert_to_ASCII=ord(text)
encrupt = convert_to_ASCII +key
print(encrupt)
new = chr(encrupt)
print(new)

string_given = "onomatopeja"
encryption_key = 6
encrypted_string = []

encrypt = lambda string_given, encryption_key: chr(ord(string_given) + encryption_key)
for i in range(len(string_given)):
    s = encrypt(string_given[i], encryption_key)
    encrypted_string.append(s)
print(encrypted_string)