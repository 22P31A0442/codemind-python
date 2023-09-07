n = int(input())
x = len(str(n))
sq=n**2
q=sq
while q!=0:
    r = q%(10**x)
    if r==n:
        print("Automorphic Number")
        break
    else:
        print("Not an Automorphic Number")
        break
    