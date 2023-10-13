n = int(input())
a = list(map(int, input().split()))
x = sum(a)//n
s=0
for i in a:
    if i>=x:
        s=s+1
print(s)