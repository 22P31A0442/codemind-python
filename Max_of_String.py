s = input()
x=0
for i in s:
    if ord(i)>x:
        x=ord(i)
print(chr(x))