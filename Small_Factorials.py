n = int(input())
f=1
for i in range(1,n+1):
    x = int(input())
    for i in range(1, x+1):
        f=f*i
    print(f)
    f=1