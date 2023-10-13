n = int(input())
a = list(map(int, input().split()))
s=0
x = (sum(a))//n
for i in a:
    if i<=x:
        s=s+1
print(s)