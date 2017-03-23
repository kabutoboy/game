letter = raw_input()
s = ""
for l in letter:
    if l.isalpha():
        a = (ord("Z") - ord(l)) + ord("A")
        s += chr(a)
    else: 
        s += l

print(s)
