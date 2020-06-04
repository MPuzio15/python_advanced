DNAtoRNA = dict({'G': 'C',
                 'C': 'G',
                 'T': 'A',
                 'A': 'U',
                 })
key_list = list(DNAtoRNA.keys())
val_list = list(DNAtoRNA.values())

our_DNA = "gcta"
our = our_DNA.upper()
def encryption(our):
    decode = []
    for i in our:
        a = DNAtoRNA[i]
        decode.append(a)
    print(decode)
encryption(our)
