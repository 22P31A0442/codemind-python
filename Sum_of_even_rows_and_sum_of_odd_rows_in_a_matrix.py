r, c = map(int, input().split())
s=0
f=0
for i in range(r):
    a = list(map(int, input().split()))
    if i%2==0:
        s=s+sum(a)
    else:
        f=f+sum(a)
print(s, f, end=' ')

        