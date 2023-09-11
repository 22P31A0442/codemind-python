stri = input()
w = input()
s=0
f=0
for i in stri:
    s=s+1
    if i==w:
        f=f+1
        break
if f>0:
    print("True")
    print(s-1)
else:
    print("False")