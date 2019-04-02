print("Insert String:")
s = input()
lun = len(s)
out = ""
if lun < 2:
    print("Empty string")
else:
    for n in range(0,2):
        out = out + s[n]
    for n in range(0,2):
        out = out + s[lun - 2 + n]
print(out)
