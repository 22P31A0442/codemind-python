r, c = map(int, input().split())
mat = []
for i in range(r):
    a = list(map(int, input().split()))
    x = sum(a)
    print(x, end=' ')