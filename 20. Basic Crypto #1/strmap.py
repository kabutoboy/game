D = {
    'A': 'U',
    'B': 'N',
    'C': 'D',
    'D': 'W',
    'E': 'I',
    'F': 'B',
    'G': 'K',
    'H': 'Y',
    'I': 'S',
    'J': 'A',
    'K': 'C',
    'L': 'H',
    'M': 'F',
    'N': 'M',
    'O': 'E',
    'P': 'G',
    'Q': 'Z',
    'R': 'V',
    'S': 'X',
    'T': 'P',
    'U': 'L',
    'V': 'Q',
    'W': 'R',
    'X': 'J',
    'Y': 'O',
    'Z': 'T'
}
letter = raw_input()
shift = int(raw_input())
s = ""
for l in letter:
    if l.isalpha():
        a = D[l]
        s += a
    else: 
        s += l

print(s)
