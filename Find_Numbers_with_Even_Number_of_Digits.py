n = int(input())
a = list(map(int, input().split()))
s=0
f=0
for i in a:
    while i!=0:
        r=i%10
        s=s+1
        i=i//10
    if s%2==0:
        f=f+1
    s=0
print(f)