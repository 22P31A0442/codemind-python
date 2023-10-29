n = int(input())
a = list(map(int, input().split()))
x = a[:n//2]
y = a[n//2:]
for j in y[::-1]:
    print(j, end=' ')
for i in x:
    print(i, end=' ')
