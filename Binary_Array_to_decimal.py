n = int(input())
a = list(map(int, input().split()))
x=n-1
s=0
for i in range(0, n):
    s = s+(a[i]*(2**(x-i)))
print(s)