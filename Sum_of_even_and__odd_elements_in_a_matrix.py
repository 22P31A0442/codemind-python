r, c = map(int, input().split())
matrix = []
s=0
f=0
for i in range(r):
    a = list(map(int, input().split()))
    matrix.append(a)
for a in matrix:
    for j in a:
        if j%2==0:
            s=s+j
        else:
            f=f+j
print(s,f ,sep=' ')