codes = [0x70,
0x69,
0x63,
0x6f,
0x43,
0x54,
0x46,
0x7b,
0x41,
0x53,
0x43,
0x49,
0x49,
0x5f,
0x49,
0x53,
0x5f,
0x45,
0x41,
0x53,
0x59,
0x5f,
0x33,
0x43,
0x46,
 0x34,
0x42,
0x46,
0x41,
0x44,
0x7d]

flag = ""
for c in codes:
    flag += chr(c)

print(flag)