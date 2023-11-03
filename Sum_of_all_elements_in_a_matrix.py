r, c = map(int, input().split())
matrix =[]
s=0
for i in range(r):
    a = list(map(int, input().split()))
    matrix.append(a)
for a in matrix:
    for j in a:
        s=s+j
print(s)