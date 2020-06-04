MORSE_CODE_DICT =dict({ 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'})


print(MORSE_CODE_DICT['S'])
print(MORSE_CODE_DICT['O'])
message = input("Insert some text: ")
message = message.upper()
def encryption(message):
    for i in message:
        print(MORSE_CODE_DICT[i], end='')

encryption(message)

key_list = list(MORSE_CODE_DICT.keys())
val_list = list(MORSE_CODE_DICT.values())
morse_kod='...'
print(key_list[val_list.index(morse_kod)])
'''
'''
longer_message = ['-.-.', '---', '-..', '.', '-...', '.-.', '.-', '..', '-.', '.', '.-.', '...']



def decode (message):
    tab = []
    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    for i in message:
        a = key_list[val_list.index(i)]
        tab.append(a)
    return tab

print(decode(longer_message))




