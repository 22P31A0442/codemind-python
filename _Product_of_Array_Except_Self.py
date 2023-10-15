n = int(input())
a = list(map(int, input().split()))
f=1
for i in a:
    f=f*i
for j in a:
    print(f//j, end=' ')