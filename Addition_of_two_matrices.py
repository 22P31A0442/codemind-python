r = int(input())
matrix = []
matrix1 = []
s=0
for i in range(r):
    a = list(map(int, input().split()))
    matrix.append(a)
for j in range(r):
    a = list(map(int, input().split()))
    matrix1.append(a)
for a in range(r):
    for b in range(r):
        print(matrix[a][b]+matrix1[a][b], end=' ')
    print()