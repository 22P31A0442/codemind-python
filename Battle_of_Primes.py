a = int(input())
b = int(input())
x = a+b
s=0
f=0
while True:
    s=s+1
    y = x+s
    for i in range(1, y+1):
        if y%i==0:
            f=f+1
    if f==2:
        break
    f=0
print(s)