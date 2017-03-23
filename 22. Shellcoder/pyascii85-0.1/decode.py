import base64
import fileinput

s = ''
for line in fileinput.input():
    s += line

arr = bytearray(map(ord, s))

encoded = base64.a85decode(arr)

print(encoded)
