letter = raw_input()
shift = int(raw_input())
s = ""
for l in letter:
    if l.isalpha():
        a = (ord(l) - ord('A') + shift) % 26 + ord('A')
        s += chr(a)
    else: 
        s += l

print(s)
