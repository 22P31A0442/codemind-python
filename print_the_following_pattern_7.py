n = int(input())
for i in range(1, n+1):
    for j in range(1, n-1):
        print(j,end='')
    for z in range(1, n-2):
        print(z, end='')
    print()