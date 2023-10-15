n = int(input())
a = list(map(int,input().split()))
s=0
f=0
for i in a:
    if i%2==0:
        s=s+1
    else:
        f=f+1
print(s, end=' ')
print(f, end=' ')