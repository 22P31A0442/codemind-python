n = int(input())
a = list(map(int, input().split()))
s=0
for i in range(1, n-1):
    if a[i]%2!=0:
        if a[i+1]%2!=0 and a[i-1]%2!=0:
            s=s+1
print(s)