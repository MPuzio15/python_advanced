stringGiven = '''No man is an island,
Entire of itself.
Each is a piece of the continent,
A part of the main.
If a clod be washed away by the sea,
Europe is the less.
As well as if a promontory were.
As well as if a manor of thine own
Or of thine friend's were.
Each man's death diminishes me,
For I am involved in mankind.
Therefore, send not to know
For whom the bell tolls,
It tolls for thee.'''

encryptionKey=3
encryptedString = []
initialString =[]

#convert to ASCII decimal number and then add the key given, then convert it back to string

#encryptionFunction = lambda stringGiven, encryptionKey: chr(ord(stringGiven)+encryptionKey)
def encryptionFunction(stringGiven, encryptionKey):
    l = ord(stringGiven)+encryptionKey
    return chr(l)

for i in range(len(stringGiven)):
    s = encryptionFunction(stringGiven[i],encryptionKey)
    encryptedString.append(s)

encryptedString = "".join(encryptedString)
print(f"Encrypted string: {encryptedString} ")

key2 = -encryptionKey

for i in range(len(encryptedString)):
    s = encryptionFunction(encryptedString[i],key2)
    initialString.append(s)

initialString = ''.join(initialString)
print(f"Decoded string: {initialString} ")