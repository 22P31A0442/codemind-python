n = int(input())
av = 65
for i in range(1, n+1):
    for j in range(1, n+1):
        print(chr(av),end=' ')
    av=av+1
    print()
        