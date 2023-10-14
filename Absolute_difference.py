n = int(input())
a = list(map(int, input().split()))
s=0
f=0
x=1
y=1
for i in a:
    for j in range(1, i+1):
        if i%j==0:
            s=s+1
    if s==2:
        x = x*i
    else:
        y = y*i
    s=0
print(abs(x-y))